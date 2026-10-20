# Range-Scalp Bot

*Updated Tue Oct 20 03:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25021 | 21784 | 3237 (31) | 4 | $-7323.42 | -4.6% |
| **+10¢** | 18822 | 15084 | 3738 (46) | 4 | $-6491.53 | -5.5% |
| **+15¢** | 15751 | 11725 | 4026 (70) | 4 | $-5848.79 | -5.9% |
| **+20¢** | 13926 | 9711 | 4215 (88) | 4 | $-5250.01 | -6.0% |
| **+10¢ (15¢ stop)** | 30704 | 30652 | 52 (30) | 3 | $-11432.04 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 03:25 | +10 stop | ETH | DOWN | 0.57 | open |  |
| 10-20 03:25 | +10 stop | NEAR | DOWN | 0.54 | open |  |
| 10-20 03:25 | +10 stop | DOGE | DOWN | 0.66 | open |  |
| 10-20 03:25 | +20 | DOGE | DOWN | 0.66 | open |  |
| 10-20 03:25 | +15 | DOGE | DOWN | 0.66 | open |  |
| 10-20 03:25 | +10 | DOGE | DOWN | 0.66 | open |  |
| 10-20 03:25 | +5 | DOGE | DOWN | 0.66 | open |  |
| 10-20 03:24 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 10-20 03:24 | +10 stop | NEAR | UP | 0.63 | 0.47 | -1.95 |
| 10-20 03:23 | +10 stop | ETH | UP | 0.69 | 0.53 | -1.93 |
| 10-20 03:23 | +20 | ETH | UP | 0.69 | open |  |
| 10-20 03:23 | +15 | ETH | UP | 0.69 | open |  |
| 10-20 03:23 | +10 | ETH | UP | 0.69 | open |  |
| 10-20 03:23 | +5 | ETH | UP | 0.69 | open |  |
| 10-20 03:23 | +10 stop | BTC | DOWN | 0.57 | 0.73 | 1.28 |
| 10-20 03:23 | +20 | BTC | DOWN | 0.57 | 0.82 | 2.21 |
| 10-20 03:23 | +15 | BTC | DOWN | 0.57 | 0.73 | 1.28 |
| 10-20 03:23 | +10 | BTC | DOWN | 0.57 | 0.73 | 1.28 |
| 10-20 03:23 | +5 | BTC | DOWN | 0.57 | 0.64 | 0.35 |
| 10-20 03:22 | +10 stop | BNB | UP | 0.61 | 0.45 | -1.97 |
| 10-20 03:22 | +10 stop | NEAR | DOWN | 0.62 | 0.32 | -3.29 |
| 10-20 03:22 | +15 | NEAR | DOWN | 0.62 | open |  |
| 10-20 03:22 | +10 | NEAR | DOWN | 0.62 | open |  |
| 10-20 03:22 | +5 | NEAR | DOWN | 0.62 | open |  |
| 10-20 03:21 | +5 | BNB | DOWN | 0.51 | open |  |
| 10-20 03:20 | +5 | BNB | DOWN | 0.56 | 0.62 | 0.25 |
| 10-20 03:19 | +5 | BNB | DOWN | 0.54 | 0.60 | 0.25 |
| 10-20 03:17 | +5 | NEAR | DOWN | 0.66 | 0.73 | 0.40 |
| 10-20 03:17 | +10 stop | BNB | DOWN | 0.58 | 0.40 | -2.15 |
| 10-20 03:17 | +20 | BNB | DOWN | 0.58 | open |  |
| 10-20 03:17 | +15 | BNB | DOWN | 0.58 | open |  |
| 10-20 03:17 | +10 | BNB | DOWN | 0.58 | open |  |
| 10-20 03:17 | +5 | BNB | DOWN | 0.58 | 0.64 | 0.25 |
| 10-20 03:16 | +10 stop | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 10-20 03:16 | +20 | NEAR | DOWN | 0.59 | open |  |
| 10-20 03:16 | +15 | NEAR | DOWN | 0.59 | 0.76 | 1.40 |
| 10-20 03:16 | +10 | NEAR | DOWN | 0.57 | 0.67 | 0.66 |
| 10-20 03:16 | +5 | NEAR | DOWN | 0.57 | 0.62 | 0.15 |
| 10-20 03:16 | +10 stop | ETH | DOWN | 0.63 | 0.79 | 1.31 |
| 10-20 03:16 | +20 | ETH | DOWN | 0.63 | 0.85 | 1.94 |
