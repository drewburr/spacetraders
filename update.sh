if [ -f "poetry.lock" ]; then
    poetry update --with dev
else
    poetry install --with dev --no-root
fi
