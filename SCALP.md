# Range-Scalp Bot

*Updated Thu Nov 05 13:48 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48341 | 42116 | 6225 (73) | 3 | $-13789.89 | -4.5% |
| **+10¢** | 36093 | 28861 | 7232 (99) | 4 | $-12644.35 | -5.6% |
| **+15¢** | 30246 | 22459 | 7787 (127) | 4 | $-11532.21 | -6.1% |
| **+20¢** | 26870 | 18712 | 8158 (166) | 4 | $-10185.49 | -6.0% |
| **+10¢ (15¢ stop)** | 58918 | 58825 | 93 (56) | 3 | $-21869.11 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 13:48 | +10 stop | DOGE | UP | 0.68 | open |  |
| 11-05 13:48 | +20 | DOGE | UP | 0.68 | open |  |
| 11-05 13:48 | +15 | DOGE | UP | 0.68 | open |  |
| 11-05 13:48 | +10 | DOGE | UP | 0.68 | open |  |
| 11-05 13:48 | +5 | DOGE | UP | 0.68 | open |  |
| 11-05 13:47 | +10 stop | XRP | UP | 0.69 | open |  |
| 11-05 13:47 | +20 | XRP | UP | 0.69 | open |  |
| 11-05 13:47 | +15 | XRP | UP | 0.70 | open |  |
| 11-05 13:47 | +10 | XRP | UP | 0.70 | open |  |
| 11-05 13:47 | +5 | XRP | UP | 0.70 | open |  |
| 11-05 13:46 | +10 stop | HYPE | UP | 0.71 | 0.53 | -2.13 |
| 11-05 13:46 | +20 | HYPE | UP | 0.71 | open |  |
| 11-05 13:46 | +15 | HYPE | UP | 0.71 | open |  |
| 11-05 13:46 | +10 | HYPE | UP | 0.71 | open |  |
| 11-05 13:46 | +5 | HYPE | UP | 0.71 | open |  |
| 11-05 13:45 | +10 stop | ETH | UP | 0.71 | open |  |
| 11-05 13:45 | +20 | ETH | UP | 0.71 | open |  |
| 11-05 13:45 | +15 | ETH | UP | 0.71 | open |  |
| 11-05 13:45 | +10 | ETH | UP | 0.71 | open |  |
| 11-05 13:45 | +5 | ETH | UP | 0.71 | 0.76 | 0.22 |
| 11-05 13:44 | +10 stop | SOL | DOWN | 0.57 | 0.69 | 0.87 |
| 11-05 13:44 | +5 | SOL | DOWN | 0.60 | 0.69 | 0.58 |
| 11-05 13:43 | +10 stop | DOGE | UP | 0.62 | 0.82 | 1.72 |
| 11-05 13:42 | +10 stop | SOL | UP | 0.57 | 0.15 | -4.47 |
| 11-05 13:42 | +15 | SOL | UP | 0.57 | no | -5.88 |
| 11-05 13:42 | +10 | SOL | UP | 0.57 | no | -5.88 |
| 11-05 13:42 | +5 | SOL | UP | 0.56 | 0.63 | 0.35 |
| 11-05 13:42 | +5 | BNB | UP | 0.63 | 0.69 | 0.28 |
| 11-05 13:41 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-05 13:41 | +20 | XRP | DOWN | 0.71 | 0.92 | 1.89 |
| 11-05 13:41 | +10 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-05 13:41 | +5 | XRP | DOWN | 0.69 | 0.78 | 0.62 |
| 11-05 13:41 | +10 stop | BNB | UP | 0.55 | 0.69 | 1.07 |
| 11-05 13:41 | +15 | BNB | UP | 0.55 | 0.92 | 3.51 |
| 11-05 13:41 | +10 | BNB | UP | 0.55 | 0.69 | 1.07 |
| 11-05 13:41 | +5 | BNB | UP | 0.55 | 0.61 | 0.25 |
| 11-05 13:40 | +10 stop | BTC | UP | 0.64 | 0.82 | 1.52 |
| 11-05 13:39 | +10 stop | DOGE | DOWN | 0.57 | 0.16 | -4.38 |
| 11-05 13:39 | +10 | DOGE | DOWN | 0.57 | yes | -5.88 |
| 11-05 13:39 | +5 | DOGE | DOWN | 0.57 | yes | -5.88 |
