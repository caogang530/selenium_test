@echo off
setlocal

set IMAGE_NAME=beikeshop_tester

REM 检查镜像是否存在
docker images --format "{{.Repository}}:{{.Tag}}" | findstr /C:"%IMAGE_NAME%:latest" > nul

if %errorlevel% equ 0 (
    echo Image %IMAGE_NAME%:latest already exists, skipping build.
) else (
    echo Building image %IMAGE_NAME%:latest...
    
    REM 方案1: 禁用漏洞扫描 + 禁用BuildKit (推荐)
    set DOCKER_SCOUT_DISABLE=true
    docker build -t %IMAGE_NAME% .
    
    REM 方案2: 如果方案1失败，尝试传统构建模式
    REM if %errorlevel% neq 0 (
    REM     set DOCKER_BUILDKIT=0
    REM     docker build -t %IMAGE_NAME% .
    REM )
    
    if %errorlevel% neq 0 (
        echo Build failed
        exit /b %errorlevel%
    )
    echo Image built successfully
)

endlocal