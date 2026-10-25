# Range-Scalp Bot

*Updated Sun Oct 25 16:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33345 | 29089 | 4256 (42) | 1 | $-9400.60 | -4.5% |
| **+10¢** | 24964 | 20040 | 4924 (60) | 1 | $-8349.55 | -5.3% |
| **+15¢** | 20887 | 15585 | 5302 (83) | 1 | $-7536.12 | -5.7% |
| **+20¢** | 18509 | 12958 | 5551 (105) | 1 | $-6637.87 | -5.7% |
| **+10¢ (15¢ stop)** | 40895 | 40835 | 60 (32) | 0 | $-15615.48 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 15:57 | +10 stop | DOGE | UP | 0.61 | 0.86 | 2.24 |
| 10-25 15:57 | +5 | DOGE | UP | 0.61 | 0.69 | 0.48 |
| 10-25 15:55 | +5 | DOGE | UP | 0.58 | 0.68 | 0.66 |
| 10-25 15:53 | +10 stop | BTC | UP | 0.47 | 0.27 | -2.32 |
| 10-25 15:52 | +10 stop | BNB | DOWN | 0.70 | 0.89 | 1.68 |
| 10-25 15:52 | +10 stop | SOL | DOWN | 0.63 | 0.77 | 1.10 |
| 10-25 15:52 | +10 stop | DOGE | UP | 0.70 | 0.53 | -2.03 |
| 10-25 15:52 | +20 | DOGE | UP | 0.70 | 0.99 | 2.76 |
| 10-25 15:52 | +15 | DOGE | UP | 0.70 | 0.86 | 1.36 |
| 10-25 15:52 | +10 | DOGE | UP | 0.70 | 0.86 | 1.36 |
| 10-25 15:52 | +5 | DOGE | UP | 0.70 | 0.75 | 0.21 |
| 10-25 15:52 | +10 stop | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-25 15:51 | +10 stop | BNB | DOWN | 0.57 | 0.69 | 0.83 |
| 10-25 15:51 | +10 stop | BTC | UP | 0.68 | 0.52 | -1.94 |
| 10-25 15:51 | +10 | BTC | UP | 0.68 | open |  |
| 10-25 15:50 | +10 stop | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-25 15:49 | +5 | BTC | UP | 0.65 | open |  |
| 10-25 15:48 | +10 stop | XRP | DOWN | 0.67 | 0.50 | -2.04 |
| 10-25 15:48 | +10 stop | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 10-25 15:48 | +10 | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 10-25 15:48 | +5 | DOGE | UP | 0.64 | 0.69 | 0.18 |
| 10-25 15:48 | +10 stop | ZEC | UP | 0.63 | 0.40 | -2.64 |
| 10-25 15:48 | +10 stop | BTC | UP | 0.57 | 0.67 | 0.66 |
| 10-25 15:48 | +20 | BTC | UP | 0.57 | open |  |
| 10-25 15:48 | +15 | BTC | UP | 0.57 | open |  |
| 10-25 15:48 | +10 | BTC | UP | 0.57 | 0.67 | 0.66 |
| 10-25 15:48 | +5 | BTC | UP | 0.57 | 0.64 | 0.35 |
| 10-25 15:47 | +10 stop | BNB | DOWN | 0.65 | 0.50 | -1.84 |
| 10-25 15:47 | +20 | BNB | DOWN | 0.65 | 0.89 | 2.17 |
| 10-25 15:47 | +15 | BNB | DOWN | 0.65 | 0.89 | 2.17 |
| 10-25 15:47 | +10 | BNB | DOWN | 0.65 | 0.89 | 2.17 |
| 10-25 15:47 | +5 | BNB | DOWN | 0.65 | 0.72 | 0.39 |
| 10-25 15:47 | +10 stop | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-25 15:47 | +20 | ETH | DOWN | 0.66 | 0.89 | 2.07 |
| 10-25 15:47 | +15 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 10-25 15:47 | +10 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-25 15:47 | +5 | ETH | DOWN | 0.66 | 0.73 | 0.40 |
| 10-25 15:46 | +15 | ZEC | DOWN | 0.68 | 0.84 | 1.34 |
| 10-25 15:46 | +10 | ZEC | DOWN | 0.68 | 0.82 | 1.13 |
| 10-25 15:46 | +5 | ZEC | DOWN | 0.68 | 0.75 | 0.40 |
