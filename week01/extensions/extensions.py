struct RGBTRIPLE
    rgbtRed::Int
    rgbtGreen::Int
    rgbtBlue::Int
end

function grayscale(height, width, image)
    for i in 1:height
        for j in 1:width
            average = (image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3
            gray_value = round(Int, average)
            image[i][j].rgbtRed = gray_value
            image[i][j].rgbtGreen = gray_value
            image[i][j].rgbtBlue = gray_value
        end
    end
end

function sepia(height, width, image)
    for i in 1:height
        for j in 1:width
            sepiaRed = 0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue
            sepiaGreen = 0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue
            sepiaBlue = 0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue

            sepiaRed = min(sepiaRed, 255)
            sepiaGreen = min(sepiaGreen, 255)
            sepiaBlue = min(sepiaBlue, 255)

            image[i][j].rgbtRed = round(Int, sepiaRed)
            image[i][j].rgbtGreen = round(Int, sepiaGreen)
            image[i][j].rgbtBlue = round(Int, sepiaBlue)
        end
    end
end

function reflect(height, width, image)
    for i in 1:height
        for j in 1:(div(width, 2))
            buffer = image[i][j]
            image[i][j] = image[i][width - j + 1]
            image[i][width - j + 1] = buffer
        end
    end
end

function blur(height, width, image)
    copy_image = deepcopy(image)
    for h in 1:height
        for w in 1:width
            box = RGBTRIPLE[]
            for dh in -1:1
                for dw in -1:1
                    if 1 <= h+dh <= height && 1 <= w+dw <= width
                        push!(box, image[h+dh][w+dw])
                    else
                        push!(box, RGBTRIPLE(0, 0, 0))
                    end
                end
            end
            divisor = length(box)
            averageRed = sum(pixel.rgbtRed for pixel in box) / divisor
            averageGreen = sum(pixel.rgbtGreen for pixel in box) / divisor
            averageBlue = sum(pixel.rgbtBlue for pixel in box) / divisor

            copy_image[h][w].rgbtRed = round(Int, averageRed)
            copy_image[h][w].rgbtGreen = round(Int, averageGreen)
            copy_image[h][w].rgbtBlue = round(Int, averageBlue)
        end
    end

    for a in 1:height
        for b in 1:width
            image[a][b] = copy_image[a][b]
        end
    end
end

