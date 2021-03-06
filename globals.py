# coding=utf-8
# 所有私聊消息没加好友的话发不出去，没有临时会话的 API

enable_group_in_auto_check = True
# 如果为真，会自动将学号姓名正确的批准加群
card_pattern = R"\d{2}[\-－ ]*[\u4e00-\u9fa5]+.*"
# 群名片 pattern

prohibited_duration = 10
# 关键词 ban 的时间 / min

prompts = dict(
    ping='pong!',
    why_at_me='干嘛？',
    unknown_command='未知命令，请输入%help或%menu查看命令',
    need_more_arguments='缺少必要参数',
    must_digits_or_CQat='参数必须是 QQ 号或者一次成功的 @人',
    must_digits='参数必须是正整数',
    wrong_argument='参数错误',
    permission_needed='你没有执行此命令的权限',
    code_too_long='代码这么长？贴到 https://paste.ubuntu.com 再发上来',
    msg_too_long='小伙子你有刷屏嫌疑呐',
    group_request_plz_fill='必须完整填写你的学号姓名',
    group_request_plz_correct='请正确填写你的学号姓名',
    request_change_card='你的群名片不符合规范，请按照 年级-专业-姓名 的格式修改，注意用英文连接符。',
    kick_for_card_incorrect='由于你的群名片不符合规范，你已被移出群\n'
                            '因为群昵称更新的频率很低，误判也不是不可能\n'
                            '如果因此对你进行了误操作，十分抱歉，重新加群即可~',
    forever_ban_private="你已被永久禁言，如有异议，请私戳管理员",
    success_ban='禁言成功，[CQ:at,qq={to}] 将被禁言 {duration} 分钟',
    success_whole_ban='已开启全员禁言，有权限的人可私聊回复 %unban 群号 解除全员禁言',
    success_unban='解禁成功，对 [CQ:at,qq={to}] 的禁言已被撤销',
    success_whole_unban='全员禁言已关闭',
    success_auto_check_card='群名片检查完毕',
    printf_crash='皮，那边好像崩了',
    shellcode_crash='不仅失败了，还把程序跑崩了，真滴过分',
    bonus_create_code_succeed='%s个激活码生成完毕,当前共有激活码%s个',
    bonus_create_code_failed='生成失败，请保证一次生成数量不超过20，且当前激活码总量不超过100',
    bonus_get_bonus_succeed='恭喜你成功领取一个星球杯! 你当前共有星球杯%s个',
    bonus_get_bonus_failed='错误的激活码或你没有权限领取',
    bonus_sqlite_error='sqlite Error:%s',
    bonus_help='\n'.join(['bonus 指令用于领取星球杯福利，具体操作如下:',
                          'init  用来初始化数据库，该指令将会创建用户表和激活码表',
                          'create + n  用来生成n个激活码，n不大于20，且数据库激活码总量不能大于200',
                          'show  用来输出激活码',
                          'help  你现在看到的',
                          '直接加激活码   验证激活码领取星球杯福利']),
    gal_deleted='游戏存档已删除',
    gal_too_many_players='当前游戏人数已达上限，请等待游戏结束',
    gal_new_best='最佳玩家记录已刷新，bad end之后的玩家将更新记录到此处',
    gal_restore_best='已将您的进度恢复到最佳玩家的记录状态，具体为Day{}，您可以继续游戏！',
    gal_all_passed='全员通关恭喜！游戏存档已清空，已经可以开始下一轮游戏',
    gal_not_here='为避免刷屏，请加群{}体验',
    gal_help='\n'.join(['galbot_v0.1——',
                        '欢迎进入大型多人在线Galgame，通称MMOGAL',
                        '使用%gal命令可以开始游戏，进入下一关也请使用这条命令',
                        '每个人的游戏进度单独记录，请直接输入选项中的文字进行回答',
                        '现版本只实装了火车游戏(前半段)，请互相配合合理利用信息过关',
                        '您可以使用%gal help再次查看这条帮助']),
    menu='\n'.join(['支持以下命令',
                    '%ban* [QQ/@/all] [分钟]',
                    '禁言，默认2min，all代表全员禁言',
                    '%unban* [QQ/@/all]',
                    '解除禁言，all代表关闭全员禁言',
                    '%autocheck* [to] 与 %autokick*',
                    '检测群名片规范与否，前者@人提醒，后者直接踢人',
                    '慎用，因为群名片很久才会更新一次',
                    'to参数可填public或private，即群里或私聊提醒，默认群里',
                    '%bonus %gal %shellcode',
                    '详见对应的help选项',
                    '%menu %ping %printf',
                    '懒得解释\n',
                    '标*号者需要权限']),
    welcome_newbie="Hi，欢迎加入 Vidar-Team 2018 新生群 XD\n\n"
                   "请先阅读以下事项：\n\n"
                   "* 协会官网: https://vidar.club\n"
                   "* wiki：https://wiki.vidar.club/doku.php\n"
                   "* drops：https://drops.vidar.club/\n\n"
                   "* 为了让大家更好的相互了解，请先更改一下群名片，备注格式为18-专业-姓名\n"
                   "* 如有任何疑问，请在群里艾特管理员提问",
)

permission_commands = ["ban", "unban", "autocheck", "autokick", "debug_get_all_member"]

info_check_url = 'http://hdu.sunnysport.org.cn/api/student/info/{}'
