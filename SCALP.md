# Range-Scalp Bot

*Updated Sat Oct 24 01:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31223 | 27208 | 4015 (40) | 8 | $-9030.73 | -4.6% |
| **+10¢** | 23365 | 18728 | 4637 (58) | 9 | $-8014.57 | -5.5% |
| **+15¢** | 19549 | 14563 | 4986 (81) | 9 | $-7187.25 | -5.9% |
| **+20¢** | 17319 | 12097 | 5222 (103) | 9 | $-6418.24 | -5.9% |
| **+10¢ (15¢ stop)** | 38311 | 38252 | 59 (32) | 8 | $-14594.58 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 01:33 | +5 | DOGE | DOWN | 0.52 | 0.58 | 0.24 |
| 10-24 01:33 | +10 stop | BTC | DOWN | 0.62 | open |  |
| 10-24 01:33 | +10 stop | BNB | UP | 0.58 | open |  |
| 10-24 01:33 | +10 stop | SOL | UP | 0.65 | open |  |
| 10-24 01:32 | +10 stop | ETH | UP | 0.62 | open |  |
| 10-24 01:32 | +10 stop | DOGE | DOWN | 0.52 | open |  |
| 10-24 01:32 | +20 | DOGE | DOWN | 0.52 | open |  |
| 10-24 01:32 | +15 | DOGE | DOWN | 0.52 | open |  |
| 10-24 01:32 | +10 | DOGE | DOWN | 0.52 | open |  |
| 10-24 01:32 | +5 | DOGE | DOWN | 0.52 | 0.57 | 0.14 |
| 10-24 01:32 | +5 | SOL | UP | 0.65 | open |  |
| 10-24 01:32 | +10 stop | NEAR | UP | 0.60 | open |  |
| 10-24 01:32 | +10 stop | HYPE | UP | 0.67 | open |  |
| 10-24 01:32 | +10 stop | ZEC | UP | 0.71 | open |  |
| 10-24 01:32 | +10 stop | SOL | DOWN | 0.62 | 0.42 | -2.35 |
| 10-24 01:32 | +20 | SOL | DOWN | 0.62 | open |  |
| 10-24 01:32 | +15 | SOL | DOWN | 0.62 | open |  |
| 10-24 01:32 | +10 | SOL | DOWN | 0.62 | open |  |
| 10-24 01:32 | +5 | SOL | DOWN | 0.62 | 0.68 | 0.27 |
| 10-24 01:31 | +10 stop | ETH | DOWN | 0.68 | 0.51 | -2.04 |
| 10-24 01:31 | +20 | ETH | DOWN | 0.68 | open |  |
| 10-24 01:31 | +15 | ETH | DOWN | 0.68 | open |  |
| 10-24 01:31 | +10 | ETH | DOWN | 0.68 | open |  |
| 10-24 01:31 | +5 | ETH | DOWN | 0.68 | open |  |
| 10-24 01:30 | +10 stop | ZEC | DOWN | 0.64 | 0.44 | -2.36 |
| 10-24 01:30 | +20 | ZEC | DOWN | 0.64 | open |  |
| 10-24 01:30 | +15 | ZEC | DOWN | 0.64 | open |  |
| 10-24 01:30 | +10 | ZEC | DOWN | 0.64 | open |  |
| 10-24 01:30 | +5 | ZEC | DOWN | 0.64 | open |  |
| 10-24 01:30 | +10 stop | BNB | DOWN | 0.68 | 0.51 | -2.04 |
| 10-24 01:30 | +20 | BNB | DOWN | 0.68 | open |  |
| 10-24 01:30 | +15 | BNB | DOWN | 0.68 | open |  |
| 10-24 01:30 | +10 | BNB | DOWN | 0.68 | open |  |
| 10-24 01:30 | +5 | BNB | DOWN | 0.68 | open |  |
| 10-24 01:30 | +10 stop | HYPE | DOWN | 0.67 | 0.52 | -1.84 |
| 10-24 01:30 | +20 | HYPE | DOWN | 0.67 | open |  |
| 10-24 01:30 | +15 | HYPE | DOWN | 0.67 | open |  |
| 10-24 01:30 | +10 | HYPE | DOWN | 0.67 | open |  |
| 10-24 01:30 | +5 | HYPE | DOWN | 0.67 | open |  |
| 10-24 01:30 | +10 stop | XRP | DOWN | 0.65 | 0.37 | -3.13 |
