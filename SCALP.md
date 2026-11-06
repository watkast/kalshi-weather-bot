# Range-Scalp Bot

*Updated Fri Nov 06 21:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49982 | 43571 | 6411 (76) | 2 | $-14025.54 | -4.5% |
| **+10¢** | 37309 | 29852 | 7457 (102) | 2 | $-12900.52 | -5.5% |
| **+15¢** | 31248 | 23211 | 8037 (131) | 2 | $-11808.07 | -6.0% |
| **+20¢** | 27781 | 19355 | 8426 (172) | 3 | $-10431.42 | -6.0% |
| **+10¢ (15¢ stop)** | 60896 | 60797 | 99 (58) | 1 | $-22564.98 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 21:25 | +10 stop | DOGE | UP | 0.58 | open |  |
| 11-06 21:25 | +20 | DOGE | UP | 0.59 | open |  |
| 11-06 21:25 | +15 | DOGE | UP | 0.59 | open |  |
| 11-06 21:25 | +10 | DOGE | UP | 0.59 | open |  |
| 11-06 21:25 | +5 | DOGE | UP | 0.59 | open |  |
| 11-06 21:25 | +10 stop | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 11-06 21:25 | +20 | BTC | DOWN | 0.70 | 0.91 | 1.88 |
| 11-06 21:25 | +15 | BTC | DOWN | 0.70 | 0.86 | 1.36 |
| 11-06 21:25 | +10 | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 11-06 21:25 | +5 | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 11-06 21:23 | +10 stop | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 11-06 21:23 | +10 stop | ZEC | UP | 0.62 | 0.73 | 0.79 |
| 11-06 21:23 | +15 | ZEC | UP | 0.62 | 0.82 | 1.72 |
| 11-06 21:23 | +10 | ZEC | UP | 0.62 | 0.73 | 0.79 |
| 11-06 21:23 | +5 | ZEC | UP | 0.62 | 0.73 | 0.79 |
| 11-06 21:22 | +10 stop | NEAR | UP | 0.66 | 0.48 | -2.14 |
| 11-06 21:22 | +20 | NEAR | UP | 0.66 | open |  |
| 11-06 21:22 | +15 | NEAR | UP | 0.66 | open |  |
| 11-06 21:22 | +10 | NEAR | UP | 0.66 | open |  |
| 11-06 21:22 | +5 | NEAR | UP | 0.66 | open |  |
| 11-06 21:19 | +10 stop | NEAR | DOWN | 0.54 | 0.34 | -2.34 |
| 11-06 21:19 | +10 stop | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 11-06 21:19 | +20 | BNB | DOWN | 0.63 | 0.86 | 2.04 |
| 11-06 21:19 | +15 | BNB | DOWN | 0.63 | 0.86 | 2.04 |
| 11-06 21:19 | +10 | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 11-06 21:19 | +5 | BNB | DOWN | 0.63 | 0.73 | 0.69 |
| 11-06 21:19 | +5 | ZEC | UP | 0.64 | 0.73 | 0.59 |
| 11-06 21:18 | +5 | HYPE | UP | 0.64 | 0.84 | 1.73 |
| 11-06 21:18 | +5 | XRP | UP | 0.69 | 0.74 | 0.21 |
| 11-06 21:18 | +10 stop | NEAR | UP | 0.64 | 0.44 | -2.35 |
| 11-06 21:18 | +10 | NEAR | UP | 0.64 | 0.78 | 1.10 |
| 11-06 21:18 | +5 | NEAR | UP | 0.64 | 0.69 | 0.18 |
| 11-06 21:17 | +5 | NEAR | UP | 0.57 | 0.62 | 0.15 |
| 11-06 21:16 | +10 stop | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 11-06 21:16 | +20 | DOGE | UP | 0.63 | 0.84 | 1.83 |
| 11-06 21:16 | +15 | DOGE | UP | 0.63 | 0.80 | 1.41 |
| 11-06 21:16 | +10 | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 11-06 21:16 | +5 | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 11-06 21:16 | +10 stop | ETH | DOWN | 0.52 | 0.73 | 1.78 |
| 11-06 21:16 | +20 | ETH | DOWN | 0.52 | 0.73 | 1.78 |
