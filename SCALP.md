# Range-Scalp Bot

*Updated Wed Oct 14 22:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16634 | 14419 | 2215 (28) | 6 | $-5211.37 | -5.0% |
| **+10¢** | 12583 | 10017 | 2566 (40) | 6 | $-4757.35 | -6.0% |
| **+15¢** | 10571 | 7815 | 2756 (59) | 6 | $-4274.08 | -6.4% |
| **+20¢** | 9392 | 6504 | 2888 (76) | 6 | $-3780.12 | -6.4% |
| **+10¢ (15¢ stop)** | 20487 | 20437 | 50 (29) | 2 | $-7885.45 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 22:37 | +10 stop | ZEC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-14 22:37 | +10 | ZEC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-14 22:37 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 10-14 22:37 | +5 | ZEC | DOWN | 0.59 | 0.66 | 0.37 |
| 10-14 22:37 | +10 stop | DOGE | DOWN | 0.61 | open |  |
| 10-14 22:37 | +10 stop | ETH | DOWN | 0.65 | 0.48 | -2.04 |
| 10-14 22:37 | +10 | ETH | DOWN | 0.65 | open |  |
| 10-14 22:37 | +5 | ETH | DOWN | 0.65 | open |  |
| 10-14 22:36 | +10 stop | ZEC | DOWN | 0.50 | 0.61 | 0.75 |
| 10-14 22:36 | +20 | ZEC | DOWN | 0.50 | 0.75 | 2.18 |
| 10-14 22:36 | +15 | ZEC | DOWN | 0.50 | 0.66 | 1.26 |
| 10-14 22:36 | +10 | ZEC | DOWN | 0.50 | 0.61 | 0.75 |
| 10-14 22:36 | +5 | ZEC | DOWN | 0.50 | 0.57 | 0.34 |
| 10-14 22:35 | +10 stop | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-14 22:35 | +10 stop | DOGE | DOWN | 0.67 | 0.51 | -1.94 |
| 10-14 22:35 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-14 22:35 | +10 stop | BNB | UP | 0.53 | 0.35 | -2.16 |
| 10-14 22:35 | +20 | BNB | UP | 0.53 | open |  |
| 10-14 22:35 | +15 | BNB | UP | 0.53 | open |  |
| 10-14 22:35 | +10 | BNB | UP | 0.53 | open |  |
| 10-14 22:35 | +5 | BNB | UP | 0.53 | open |  |
| 10-14 22:35 | +10 stop | ETH | UP | 0.48 | 0.59 | 0.75 |
| 10-14 22:35 | +15 | ETH | UP | 0.48 | open |  |
| 10-14 22:35 | +10 | ETH | UP | 0.48 | 0.59 | 0.75 |
| 10-14 22:35 | +5 | ETH | UP | 0.48 | 0.55 | 0.34 |
| 10-14 22:35 | +5 | DOGE | UP | 0.56 | open |  |
| 10-14 22:34 | +10 stop | DOGE | UP | 0.57 | 0.40 | -2.05 |
| 10-14 22:34 | +10 stop | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 10-14 22:34 | +5 | DOGE | UP | 0.56 | 0.62 | 0.25 |
| 10-14 22:34 | +5 | XRP | UP | 0.55 | open |  |
| 10-14 22:33 | +5 | DOGE | UP | 0.65 | 0.74 | 0.60 |
| 10-14 22:32 | +5 | BTC | UP | 0.67 | open |  |
| 10-14 22:32 | +10 stop | HYPE | UP | 0.65 | 0.50 | -1.88 |
| 10-14 22:32 | +20 | HYPE | UP | 0.65 | open |  |
| 10-14 22:32 | +15 | HYPE | UP | 0.65 | open |  |
| 10-14 22:32 | +10 | HYPE | UP | 0.65 | open |  |
| 10-14 22:32 | +5 | HYPE | UP | 0.65 | open |  |
| 10-14 22:32 | +5 | BTC | UP | 0.60 | 0.66 | 0.27 |
| 10-14 22:31 | +10 stop | BTC | UP | 0.61 | 0.43 | -2.15 |
| 10-14 22:31 | +20 | BTC | UP | 0.61 | open |  |
