__all__ = ['sys_mbind', 'sys_nfsservctl', 'sys_getresuid', 'sys_clone', 'sys_listxattr', 'sys_mq_notify',
           'sys_settimeofday', 'sys_timer_gettime', 'sys_capget', 'sys_setxattr', 'sys_mq_open', 'sys_getpmsg',
           'sys_open', 'sys_eventfd2', 'sys_ioctl', 'sys_geteuid32', 'sys_pipe', 'sys_reboot', 'sys_setrlimit',
           'sys_futimesat', 'sys_fdatasync', 'sys_rt_sigreturn', 'sys_sethostname', 'sys_mq_getsetattr',
           'sys_fremovexattr', 'sys_exit', 'sys_fchmodat', 'sys_llistxattr', 'sys_setfsuid32', 'sys_epoll_create',
           'sys_sigpending', 'sys_sendfile64', 'sys_epoll_ctl', 'sys_getresgid32', 'sys_pause', 'sys_inotify_rm_watch',
           'sys_epoll_wait', 'sys_sync_file_range', 'sys_iopl', 'sys_ioprio_get', 'sys_query_module', 'sys_chown32',
           'sys_get_robust_list', 'sys_delete_module', 'sys_oldstat', 'sys_fstatfs64', 'sys_setresgid', 'sys_gtty',
           'sys_openat', 'sys_geteuid', 'sys_umount', 'sys_io_cancel', 'sys_getxattr', 'sys_stat64', 'sys_tkill',
           'sys_waitid', 'sys_setpriority', 'sys_ioprio_set', 'sys_timerfd_gettime', 'sys_inotify_add_watch',
           'sys_select', 'sys_clock_gettime', 'sys_timerfd_create', 'sys_personality', 'sys_wait4',
           'sys_remap_file_pages', 'sys_lstat64', 'sys_linkat', 'sys_sched_getaffinity', 'sys_newselect',
           'sys_inotify_init1', 'sys_execve', 'sys_mknodat', 'sys_sigreturn', 'sys_setuid', 'sys_waitpid',
           'sys_truncate', 'sys_mmap', 'sys_dup3', 'sys_ftime', 'sys_read', 'sys_mkdirat', 'sys_pwritev',
           'sys_set_mempolicy', 'sys_signal', 'sys_mq_unlink', 'sys_io_getevents', 'sys_nice', 'sys_statfs',
           'sys_getsid', 'sys_move_pages', 'sys_setitimer', 'sys_fchown32', 'sys_munlock', 'sys_getegid32', 'sys_fsync',
           'sys_sigsuspend', 'sys_uselib', 'sys_mremap', 'sys_poll', 'sys_umount2', 'sys_oldlstat', 'sys_ppoll',
           'sys_oldfstat', 'sys_getcpu', 'sys_utimensat', 'sys_setfsuid', 'sys_splice', 'sys_setfsgid', 'sys_setsid',
           'sys_ssetmask', 'sys_idle', 'sys_renameat', 'sys_getuid32', 'sys_bdflush', 'sys_setfsgid32', 'sys_getgroups',
           'sys_sched_rr_get_interval', 'sys_pipe2', 'sys_stty', 'sys_lremovexattr', 'sys_access', 'sys_mincore',
           'sys_vm86old', 'sys_timerfd_settime', 'sys_syslog', 'sys_setgid', 'sys_symlinkat', 'sys_get_kernel_syms',
           'sys_getrlimit', 'sys_fchown', 'sys_mmap2', 'sys_getrusage', 'sys_sendfile', 'sys_setuid32', 'sys_flock',
           'sys_lstat', 'sys_exit_group', 'sys_readlink', 'sys_getcwd', 'sys_prctl', 'sys_acct', 'sys_add_key',
           'sys_rt_sigtimedwait', 'sys_brk', 'sys_fgetxattr', 'sys_preadv', 'sys_kexec_load', 'sys_init_module',
           'sys_ftruncate64', 'sys_fallocate', 'sys_utime', 'sys_get_mempolicy', 'sys_io_setup', 'sys_getgid',
           'sys_unlinkat', 'sys_kill', 'sys_afs_syscall', 'sys_tee', 'sys_setreuid', 'sys_perf_counter_open',
           'sys_fork', 'sys_close', 'sys_rt_sigaction', 'sys_dup2', 'sys_socketcall', 'sys_futex', 'sys_mkdir',
           'sys_mknod', 'sys_pwrite64', 'sys_fstat', 'sys_sigaltstack', 'sys_setpgid', 'sys_getgroups32',
           'sys_set_tid_address', 'sys_ftruncate', 'sys_readlinkat', 'sys_umask', 'sys_setregid', 'sys_pselect6',
           'sys_epoll_pwait', 'sys_setregid32', 'sys_fchmod', 'sys_timer_create', 'sys_ptrace', 'sys_ulimit',
           'sys_write', 'sys_mount', 'sys_times', 'sys_clock_settime', 'sys_uname', 'sys_setgid32', 'sys_stat',
           'sys_writev', 'sys_sched_setscheduler', 'sys_signalfd', 'sys_swapoff', 'sys_getpid', 'sys_set_thread_area',
           'sys_sched_yield', 'sys_rmdir', 'sys_chmod', 'sys_getresuid32', 'sys_getpgid', 'sys_chown',
           'sys_inotify_init', 'sys_rt_sigpending', 'sys_sched_setparam', 'sys_getdents', 'sys_link',
           'sys_lookup_dcookie', 'sys_getitimer', 'sys_stime', 'sys_create_module', 'sys_lchown32', 'sys_msync',
           'sys_fstatfs', 'sys_getgid32', 'sys_dup', 'sys_flistxattr', 'sys_rt_sigprocmask', 'sys_readv',
           'sys_setresuid', 'sys_gettid', 'sys_setreuid32', 'sys_getresgid', 'sys_timer_settime', 'sys_ugetrlimit',
           'sys_rt_sigqueueinfo', 'sys_sigprocmask', 'sys_fadvise64', 'sys_epoll_create1', 'sys_mlockall',
           'sys_get_thread_area', 'sys_sysfs', 'sys_set_robust_list', 'sys_sync', 'sys_keyctl', 'sys_putpmsg',
           'sys_getdents64', 'sys_fstatat64', 'sys_setdomainname', 'sys_prof', 'sys_readahead',
           'sys_sched_get_priority_max', 'sys_break', 'sys_setgroups', 'sys_sysinfo', 'sys_munmap', 'sys_tgkill',
           'sys_migrate_pages', 'sys_getuid', 'sys_fstat64', 'sys_truncate64', 'sys_chroot', 'sys_faccessat',
           'sys_utimes', 'sys_setgroups32', 'sys_rt_sigsuspend', 'sys_mprotect', 'sys_signalfd4', 'sys_madvise',
           'sys_lgetxattr', 'sys_sched_get_priority_min', 'sys_lock', 'sys_getpriority', 'sys_profil', 'sys_unlink',
           'sys_lseek', 'sys_fchdir', 'sys_io_submit', 'sys_ustat', 'sys_sched_setaffinity', 'sys_mlock', 'sys_madvise',
           'sys_lsetxattr', 'sys_sched_getparam', 'sys_removexattr', 'sys_sched_getscheduler', 'sys_ioperm', 'sys_vm86',
           'sys_readdir', 'sys_vfork', 'sys_getpgrp', 'sys_sysctl', 'sys_sgetmask', 'sys_mpx', 'sys_time',
           'sys_request_key', 'sys_pivot_root', 'sys_setresuid32', 'sys_fadvise64_64', 'sys_fsetxattr',
           'sys_oldolduname', 'sys_creat', 'sys_ipc', 'sys_mq_timedsend', 'sys_swapon', 'sys_pread64', 'sys_rename',
           'sys_statfs64', 'sys_nanosleep', 'sys_gettimeofday', 'sys_olduname', 'sys_symlink', 'sys_rt_tgsigqueueinfo',
           'sys_chdir', 'sys_fcntl64', 'sys_vmsplice', 'sys_alarm', 'sys_vhangup', 'sys_getegid', 'sys_clock_nanosleep',
           'sys_setresgid32', 'sys_fcntl', 'sys_eventfd', 'sys_fchownat', 'sys_clock_getres', 'sys_getppid',
           'sys_lchown', 'sys_capset', 'sys_quotactl', 'sys_sigaction', 'sys_mq_timedreceive', 'sys_adjtimex',
           'sys_unshare', 'sys_timer_getoverrun', 'sys_vserver', 'sys_modify_ldt', 'sys_llseek', 'sys_munlockall',
           'sys_io_destroy', 'sys_timer_delete', 'sys_msgrcv', 'sys_sendto', 'sys_setns', 'sys_open_by_handle_at',
           'sys_fanotify_mark', 'sys_setsockopt', 'sys_socketpair', 'sys_process_vm_readv', 'sys_shutdown',
           'sys_recvmmsg', 'sys_arch_prctl', 'sys_semctl', 'sys_process_vm_writev', 'sys_recvfrom', 'sys_epoll_ctl_old',
           'sys_fanotify_init', 'sys_sendmsg', 'sys_getsockname', 'sys_name_to_handle_at', 'sys_newfstatat',
           'sys_semop', 'sys__sysctl', 'sys_getpeername', 'sys_getsockopt', 'sys_syncfs', 'sys_shmget', 'sys_accept4',
           'sys_security', 'sys_socket', 'sys_shmat', 'sys_connect', 'sys_semget', 'sys_epoll_wait_old', 'sys_accept',
           'sys_perf_event_open', 'sys_bind', 'sys_recvmsg', 'sys_listen', 'sys_clock_adjtime', 'sys_sendmmsg',
           'sys_shmdt', 'sys_tuxcall', 'sys_restart_syscall', 'sys_semtimedop', 'sys_prlimit64', 'sys_shmctl',
           'sys_msgctl', 'sys_msgget', 'sys_msgsnd', 'sys_prlimit64'
]

by_name = {}
by_id = __all__

# Now we generate the syscall dict!
for call_id, call_name in enumerate(__all__):
    by_name[call_name] = call_id

# And copy to actually define the variables
vars().update(by_name)

translator = {
    0: (274, 237),
    1: (169, 180),
    2: (165, 118),
    3: (120, 56),
    4: (232, 194),
    5: (281, 244),
    6: (79, 164),
    7: (261, 224),
    8: (184, 125),
    9: (226, 188),
    10: (277, 240),
    11: (188, 181),
    12: (5, 2),
    13: (328, 290),
    14: (54, 16),
    15: (201, None),
    16: (42, 22),
    17: (88, 169),
    18: (75, 160),
    19: (299, 261),
    20: (148, 75),
    21: (173, 15),
    22: (74, 170),
    23: (282, 245),
    24: (237, 199),
    25: (1, 60),
    26: (306, 268),
    27: (233, 195),
    28: (215, None),
    29: (254, 213),
    30: (73, None),
    31: (239, None),
    32: (255, 233),
    33: (211, None),
    34: (29, 34),
    35: (293, 255),
    36: (256, 232),
    37: (314, 277),
    38: (110, 172),
    39: (290, 252),
    40: (167, 178),
    41: (212, None),
    42: (312, 274),
    43: (129, 176),
    44: (18, None),
    45: (269, None),
    46: (170, 119),
    47: (32, None),
    48: (295, 257),
    49: (49, 107),
    50: (22, None),
    51: (249, 210),
    52: (229, 191),
    53: (195, None),
    54: (238, 200),
    55: (284, 247),
    56: (97, 141),
    57: (289, 251),
    58: (326, 287),
    59: (292, 254),
    60: (82, 23),
    61: (265, 228),
    62: (322, 283),
    63: (136, 135),
    64: (114, 61),
    65: (257, 216),
    66: (196, None),
    67: (303, 265),
    68: (242, 204),
    69: (142, None),
    70: (332, 294),
    71: (11, 59),
    72: (297, 259),
    73: (119, None),
    74: (23, 105),
    75: (7, None),
    76: (92, 76),
    77: (90, 9),
    78: (330, 292),
    79: (35, None),
    80: (3, 0),
    81: (296, 258),
    82: (334, 296),
    83: (276, 238),
    84: (48, None),
    85: (278, 241),
    86: (247, 208),
    87: (34, None),
    88: (99, 137),
    89: (147, 124),
    90: (317, 279),
    91: (104, 38),
    92: (207, None),
    93: (151, 150),
    94: (202, None),
    95: (118, 74),
    96: (72, None),
    97: (86, 134),
    98: (163, 25),
    99: (168, 7),
    100: (52, 166),
    101: (84, None),
    102: (309, 271),
    103: (28, None),
    104: (318, 309),
    105: (320, 280),
    106: (138, 122),
    107: (313, 275),
    108: (139, 123),
    109: (66, 112),
    110: (69, None),
    111: (112, None),
    112: (302, 264),
    113: (199, None),
    114: (134, None),
    115: (216, None),
    116: (80, 115),
    117: (161, 148),
    118: (331, 293),
    119: (31, None),
    120: (236, 198),
    121: (33, 21),
    122: (218, 27),
    123: (113, None),
    124: (325, 286),
    125: (103, 103),
    126: (46, 106),
    127: (304, 266),
    128: (130, 177),
    129: (76, 97),
    130: (95, 93),
    131: (192, None),
    132: (77, 98),
    133: (187, 40),
    134: (213, None),
    135: (143, 73),
    136: (107, 6),
    137: (252, 231),
    138: (85, 89),
    139: (183, 79),
    140: (172, 157),
    141: (51, 163),
    142: (286, 248),
    143: (177, 128),
    144: (45, 12),
    145: (231, 193),
    146: (333, 295),
    147: (283, 246),
    148: (128, 175),
    149: (194, None),
    150: (324, 285),
    151: (30, 132),
    152: (275, 239),
    153: (245, 206),
    154: (47, 104),
    155: (301, 263),
    156: (37, 62),
    157: (137, 183),
    158: (315, 276),
    159: (70, 113),
    160: (336, None),
    161: (2, 57),
    162: (6, 3),
    163: (174, 13),
    164: (63, 33),
    165: (102, None),
    166: (240, 202),
    167: (39, 83),
    168: (14, 133),
    169: (181, 18),
    170: (108, 5),
    171: (186, 131),
    172: (57, 109),
    173: (205, None),
    174: (258, 218),
    175: (93, 77),
    176: (305, 267),
    177: (60, 95),
    178: (71, 114),
    179: (308, 270),
    180: (319, 281),
    181: (204, None),
    182: (94, 91),
    183: (259, 222),
    184: (26, 101),
    185: (58, None),
    186: (4, 1),
    187: (21, 165),
    188: (43, 100),
    189: (264, 227),
    190: (122, 63),
    191: (214, None),
    192: (106, 4),
    193: (146, 20),
    194: (156, 144),
    195: (321, 282),
    196: (115, 168),
    197: (20, 39),
    198: (243, 205),
    199: (158, 24),
    200: (40, 84),
    201: (15, 90),
    202: (209, None),
    203: (132, 121),
    204: (182, 92),
    205: (291, 253),
    206: (176, 127),
    207: (154, 142),
    208: (141, 78),
    209: (9, 86),
    210: (253, 212),
    211: (105, 36),
    212: (25, None),
    213: (127, 174),
    214: (198, None),
    215: (144, 26),
    216: (100, 138),
    217: (200, None),
    218: (41, 32),
    219: (234, 196),
    220: (175, 14),
    221: (145, 19),
    222: (164, 117),
    223: (224, 186),
    224: (203, None),
    225: (171, 120),
    226: (260, 223),
    227: (191, None),
    228: (178, 129),
    229: (126, None),
    230: (250, 221),
    231: (329, 291),
    232: (152, 151),
    233: (244, 211),
    234: (135, 139),
    235: (311, 273),
    236: (36, 162),
    237: (288, 250),
    238: (189, 182),
    239: (220, 217),
    240: (300, None),
    241: (121, 171),
    242: (44, None),
    243: (225, 187),
    244: (159, 146),
    245: (17, None),
    246: (81, 116),
    247: (116, 99),
    248: (91, 11),
    249: (270, 234),
    250: (294, 256),
    251: (24, 102),
    252: (197, None),
    253: (193, None),
    254: (61, 161),
    255: (307, 269),
    256: (271, 235),
    257: (206, None),
    258: (179, 130),
    259: (125, 10),
    260: (327, 289),
    261: (219, None),
    262: (230, 192),
    263: (160, 147),
    264: (53, None),
    265: (96, 140),
    266: (98, None),
    267: (10, 87),
    268: (19, 8),
    269: (133, 81),
    270: (248, 209),
    271: (62, 136),
    272: (241, 203),
    273: (150, 149),
    274: (219, 28),
    275: (227, 189),
    276: (155, 143),
    277: (235, 197),
    278: (157, 145),
    279: (101, 173),
    280: (166, None),
    281: (89, None),
    282: (190, 58),
    283: (65, 111),
    284: (149, None),
    285: (68, None),
    286: (56, None),
    287: (13, 201),
    288: (287, 249),
    289: (217, 155),
    290: (208, None),
    291: (272, None),
    292: (228, 190),
    293: (59, None),
    294: (8, 85),
    295: (117, None),
    296: (279, 242),
    297: (87, 167),
    298: (180, 17),
    299: (38, 82),
    300: (268, None),
    301: (162, 35),
    302: (78, 96),
    303: (109, None),
    304: (83, 88),
    305: (335, 297),
    306: (12, 80),
    307: (221, None),
    308: (316, 278),
    309: (27, 37),
    310: (111, 153),
    311: (50, 108),
    312: (267, 230),
    313: (210, None),
    314: (55, 72),
    315: (323, 284),
    316: (298, 260),
    317: (266, 229),
    318: (64, 110),
    319: (16, 94),
    320: (185, 126),
    321: (131, 179),
    322: (67, None),
    323: (280, 243),
    324: (124, 159),
    325: (310, 272),
    326: (262, 225),
    327: (273, 236),
    328: (123, 154),
    329: (140, None),
    330: (153, 152),
    331: (246, 207),
    332: (263, 226),
    333: (None, 70),
    334: (None, 44),
    335: (None, 308),
    336: (None, 304),
    337: (None, 301),
    338: (None, 54),
    339: (None, 53),
    340: (None, 310),
    341: (None, 48),
    342: (None, 299),
    343: (None, 158),
    344: (None, 66),
    345: (None, 311),
    346: (None, 45),
    347: (None, 214),
    348: (None, 300),
    349: (None, 46),
    350: (None, 51),
    351: (None, 303),
    352: (None, 262),
    353: (None, 65),
    354: (None, 156),
    355: (None, 52),
    356: (None, 55),
    357: (None, 306),
    358: (None, 29),
    359: (None, 288),
    360: (None, 185),
    361: (None, 41),
    362: (None, 30),
    363: (None, 42),
    364: (None, 64),
    365: (None, 215),
    366: (None, 43),
    367: (None, 298),
    368: (None, 49),
    369: (None, 47),
    370: (None, 50),
    371: (None, 305),
    372: (None, 307),
    373: (None, 67),
    374: (None, 184),
    375: (None, 219),
    376: (None, 220),
    377: (None, 302),
    378: (None, 31),
    379: (None, 71),
    380: (None, 68),
    381: (None, 69),
    382: (340, None),
}

SYSCALL_COUNT = 383