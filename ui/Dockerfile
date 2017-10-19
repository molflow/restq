from node:latest
copy  . /source
workdir /source
run npm --quiet install
run npm run build

from httpd:latest
copy --from=0 /source/build/ /usr/local/apache2/htdocs/
expose 80
