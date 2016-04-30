#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <disk.c>



//prototype functions
int make_fs(char *disk_name);
int mount_fs(char *disk_name);
int dismount_fs(char *disk_name);
int fs_create(char *name);
int fs_open(char *name);
int fs_close(int fildes);
int fs_delete(char *name);
int fs_read(int fildes, void *buf, size_t nbyte);
int fs_write(int fildes, void *buf, size_t nbyte);
int fs_get_filesize(int fildes);
int fs_lseek(int fildes, off_t offset);
int fs_truncate(int fildes, off_t length);


int main() {
  return 0;
}

int make_fs(char *disk_name){
  int result;
  return result;
}

int mount_fs(char *disk_name){
  int result;
  return result;
}

int dismount_fs(char *disk_name){
  int result;
  return result;
}

int fs_create(char *name){
  int result;
  return result;
}

int fs_open(char *name){
  int result;
  return result;
}

int fs_close(int fildes){
  int result;
  return result;
}

int fs_delete(char *name){
  int result;
  return result;
}

int fs_read(intfildes,void *buf, size_t nbyte){
  int result;
  return result;
}

int fs_write(int fildes, void *buf, size_t nbyte){
  int result;
  return result;
}

int fs_get_filesize(int fildes){
  int result;
  return result;
}

int fs_lseek(int fildes, off_t offset){
  int result;
  return result;
}

int fs_truncate(int fildes, off_t length){
  int result;
  return result;
}
