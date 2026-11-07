# Range-Scalp Bot

*Updated Sat Nov 07 10:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50890 | 44366 | 6524 (76) | 4 | $-14251.68 | -4.4% |
| **+10¢** | 37989 | 30384 | 7605 (102) | 4 | $-13229.61 | -5.5% |
| **+15¢** | 31801 | 23607 | 8194 (131) | 6 | $-12146.91 | -6.1% |
| **+20¢** | 28277 | 19689 | 8588 (173) | 6 | $-10725.35 | -6.0% |
| **+10¢ (15¢ stop)** | 61984 | 61885 | 99 (58) | 2 | $-22914.41 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 10:54 | +10 stop | ETH | UP | 0.61 | open |  |
| 11-07 10:53 | +5 | SOL | UP | 0.66 | 0.73 | 0.40 |
| 11-07 10:53 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-07 10:53 | +20 | XRP | DOWN | 0.65 | open |  |
| 11-07 10:53 | +15 | XRP | DOWN | 0.65 | open |  |
| 11-07 10:53 | +10 | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-07 10:53 | +5 | XRP | DOWN | 0.65 | 0.73 | 0.50 |
| 11-07 10:53 | +10 stop | ETH | UP | 0.55 | 0.65 | 0.66 |
| 11-07 10:52 | +10 stop | ZEC | UP | 0.65 | 0.85 | 1.75 |
| 11-07 10:52 | +10 stop | NEAR | UP | 0.63 | 0.82 | 1.62 |
| 11-07 10:52 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 11-07 10:51 | +5 | SOL | UP | 0.62 | 0.67 | 0.17 |
| 11-07 10:50 | +5 | SOL | UP | 0.50 | 0.64 | 1.05 |
| 11-07 10:50 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.71 |
| 11-07 10:50 | +10 stop | ETH | UP | 0.63 | 0.45 | -2.15 |
| 11-07 10:49 | +10 stop | NEAR | UP | 0.58 | 0.39 | -2.25 |
| 11-07 10:49 | +5 | DOGE | DOWN | 0.54 | 0.63 | 0.55 |
| 11-07 10:49 | +10 stop | ETH | DOWN | 0.43 | 0.62 | 1.55 |
| 11-07 10:49 | +10 stop | ZEC | UP | 0.58 | 0.76 | 1.49 |
| 11-07 10:48 | +5 | DOGE | DOWN | 0.52 | 0.58 | 0.24 |
| 11-07 10:48 | +10 stop | ETH | UP | 0.63 | 0.35 | -3.13 |
| 11-07 10:48 | +10 | ETH | UP | 0.63 | open |  |
| 11-07 10:48 | +5 | ETH | UP | 0.63 | open |  |
| 11-07 10:48 | +10 stop | BTC | UP | 0.68 | 0.49 | -2.24 |
| 11-07 10:48 | +20 | BTC | UP | 0.68 | open |  |
| 11-07 10:48 | +15 | BTC | UP | 0.68 | open |  |
| 11-07 10:48 | +10 | BTC | UP | 0.68 | open |  |
| 11-07 10:48 | +5 | BTC | UP | 0.68 | open |  |
| 11-07 10:47 | +10 stop | NEAR | DOWN | 0.64 | 0.44 | -2.35 |
| 11-07 10:47 | +20 | NEAR | DOWN | 0.64 | open |  |
| 11-07 10:47 | +15 | NEAR | DOWN | 0.64 | open |  |
| 11-07 10:47 | +10 | NEAR | DOWN | 0.64 | open |  |
| 11-07 10:47 | +5 | NEAR | DOWN | 0.64 | open |  |
| 11-07 10:47 | +10 stop | DOGE | DOWN | 0.54 | 0.72 | 1.47 |
| 11-07 10:47 | +20 | DOGE | DOWN | 0.54 | 0.74 | 1.68 |
| 11-07 10:47 | +15 | DOGE | DOWN | 0.54 | 0.72 | 1.47 |
| 11-07 10:47 | +10 | DOGE | DOWN | 0.54 | 0.72 | 1.47 |
| 11-07 10:47 | +5 | DOGE | DOWN | 0.54 | 0.59 | 0.15 |
| 11-07 10:47 | +10 stop | ZEC | DOWN | 0.66 | 0.50 | -1.94 |
| 11-07 10:47 | +20 | ZEC | DOWN | 0.66 | open |  |
