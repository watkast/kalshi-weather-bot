# Range-Scalp Bot

*Updated Sat Oct 24 06:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31604 | 27550 | 4054 (40) | 6 | $-9074.42 | -4.6% |
| **+10¢** | 23624 | 18942 | 4682 (58) | 8 | $-8053.73 | -5.4% |
| **+15¢** | 19777 | 14743 | 5034 (81) | 9 | $-7199.48 | -5.8% |
| **+20¢** | 17521 | 12251 | 5270 (103) | 9 | $-6390.08 | -5.8% |
| **+10¢ (15¢ stop)** | 38786 | 38727 | 59 (32) | 6 | $-14830.08 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 06:35 | +5 | BNB | UP | 0.60 | 0.65 | 0.17 |
| 10-24 06:35 | +10 stop | ZEC | UP | 0.56 | 0.38 | -2.15 |
| 10-24 06:35 | +10 | ZEC | UP | 0.56 | open |  |
| 10-24 06:35 | +10 stop | XRP | UP | 0.60 | 0.42 | -2.15 |
| 10-24 06:35 | +10 stop | HYPE | UP | 0.66 | open |  |
| 10-24 06:35 | +5 | HYPE | UP | 0.66 | open |  |
| 10-24 06:34 | +10 stop | DOGE | UP | 0.49 | open |  |
| 10-24 06:34 | +10 stop | ETH | UP | 0.61 | open |  |
| 10-24 06:34 | +10 stop | BTC | UP | 0.54 | open |  |
| 10-24 06:34 | +10 | BTC | UP | 0.54 | open |  |
| 10-24 06:34 | +5 | BTC | UP | 0.54 | open |  |
| 10-24 06:34 | +5 | NEAR | UP | 0.63 | 0.70 | 0.38 |
| 10-24 06:33 | +10 stop | NEAR | UP | 0.61 | 0.72 | 0.78 |
| 10-24 06:33 | +10 stop | HYPE | DOWN | 0.47 | 0.57 | 0.64 |
| 10-24 06:33 | +5 | HYPE | DOWN | 0.48 | 0.57 | 0.52 |
| 10-24 06:33 | +5 | BNB | UP | 0.60 | 0.67 | 0.38 |
| 10-24 06:33 | +10 stop | DOGE | DOWN | 0.58 | 0.39 | -2.25 |
| 10-24 06:33 | +5 | NEAR | UP | 0.51 | 0.59 | 0.45 |
| 10-24 06:33 | +10 stop | SOL | DOWN | 0.64 | open |  |
| 10-24 06:33 | +10 | SOL | DOWN | 0.64 | open |  |
| 10-24 06:33 | +5 | SOL | DOWN | 0.64 | 0.70 | 0.28 |
| 10-24 06:33 | +5 | BNB | UP | 0.57 | 0.63 | 0.25 |
| 10-24 06:32 | +15 | ETH | UP | 0.54 | open |  |
| 10-24 06:32 | +10 stop | DOGE | UP | 0.66 | 0.50 | -1.94 |
| 10-24 06:32 | +10 | DOGE | UP | 0.66 | open |  |
| 10-24 06:32 | +5 | DOGE | UP | 0.66 | open |  |
| 10-24 06:32 | +5 | XRP | UP | 0.64 | open |  |
| 10-24 06:32 | +5 | ZEC | UP | 0.65 | open |  |
| 10-24 06:32 | +5 | BTC | UP | 0.57 | 0.62 | 0.15 |
| 10-24 06:31 | +10 stop | ETH | UP | 0.64 | 0.43 | -2.45 |
| 10-24 06:31 | +10 | ETH | UP | 0.64 | open |  |
| 10-24 06:31 | +5 | ETH | UP | 0.65 | open |  |
| 10-24 06:31 | +10 stop | ZEC | UP | 0.54 | 0.64 | 0.65 |
| 10-24 06:31 | +20 | ZEC | UP | 0.54 | open |  |
| 10-24 06:31 | +15 | ZEC | UP | 0.54 | open |  |
| 10-24 06:31 | +10 | ZEC | UP | 0.54 | 0.64 | 0.65 |
| 10-24 06:31 | +5 | ZEC | UP | 0.54 | 0.63 | 0.55 |
| 10-24 06:31 | +10 stop | ETH | UP | 0.53 | 0.64 | 0.75 |
| 10-24 06:31 | +20 | ETH | UP | 0.53 | open |  |
| 10-24 06:31 | +15 | ETH | UP | 0.53 | 0.69 | 1.27 |
