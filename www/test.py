import www.orm, asyncio
from www.models import User, Blog, Comment


async def test(loop):
    await www.orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    u = User(name='wtf', email='6', passwd='000', image='about:blank')
    await u.save()


async def find(loop):
    await www.orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    rs = await User.findAll()
    print('查找测试： %s' % rs)


async def delete(loop, email=None):

    await www.orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    id = await User.findNumber('id', where='email="'+email+'"')
    u = User(id=id)
    await u.remove()
    print('删除测试： %s' % id)

loop2 = asyncio.get_event_loop()
loop2.run_until_complete(asyncio.wait([test(loop2), find(loop2), delete(loop2, email='6')]))
loop2.run_forever()