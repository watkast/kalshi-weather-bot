# Range-Scalp Bot

*Updated Tue Oct 20 08:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25342 | 22070 | 3272 (31) | 0 | $-7379.29 | -4.6% |
| **+10¢** | 19072 | 15290 | 3782 (46) | 0 | $-6543.12 | -5.5% |
| **+15¢** | 15962 | 11888 | 4074 (70) | 0 | $-5885.53 | -5.9% |
| **+20¢** | 14109 | 9844 | 4265 (88) | 0 | $-5276.54 | -6.0% |
| **+10¢ (15¢ stop)** | 31096 | 31044 | 52 (30) | 0 | $-11517.95 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 07:55 | +10 stop | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-20 07:55 | +10 stop | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-20 07:55 | +5 | BNB | DOWN | 0.65 | 0.79 | 1.12 |
| 10-20 07:54 | +10 stop | DOGE | UP | 0.54 | 0.68 | 1.06 |
| 10-20 07:54 | +10 stop | ETH | DOWN | 0.70 | 0.91 | 1.83 |
| 10-20 07:54 | +20 | ETH | DOWN | 0.70 | 0.91 | 1.83 |
| 10-20 07:54 | +15 | ETH | DOWN | 0.70 | 0.91 | 1.83 |
| 10-20 07:54 | +10 | ETH | DOWN | 0.70 | 0.91 | 1.83 |
| 10-20 07:54 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 10-20 07:54 | +10 stop | BNB | DOWN | 0.48 | 0.61 | 0.95 |
| 10-20 07:54 | +5 | BNB | DOWN | 0.47 | 0.53 | 0.24 |
| 10-20 07:54 | +10 stop | DOGE | DOWN | 0.39 | 0.57 | 1.45 |
| 10-20 07:53 | +10 stop | NEAR | DOWN | 0.69 | 0.51 | -2.13 |
| 10-20 07:53 | +10 stop | DOGE | UP | 0.57 | 0.33 | -2.74 |
| 10-20 07:53 | +10 stop | XRP | UP | 0.50 | 0.35 | -1.84 |
| 10-20 07:52 | +10 stop | ZEC | DOWN | 0.58 | 0.70 | 0.87 |
| 10-20 07:51 | +10 stop | SOL | DOWN | 0.62 | 0.42 | -2.35 |
| 10-20 07:50 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-20 07:50 | +10 stop | DOGE | DOWN | 0.47 | 0.31 | -1.93 |
| 10-20 07:50 | +10 stop | ETH | DOWN | 0.61 | 0.72 | 0.78 |
| 10-20 07:49 | +10 stop | BTC | DOWN | 0.70 | 0.86 | 1.36 |
| 10-20 07:49 | +10 stop | BNB | DOWN | 0.56 | 0.72 | 1.27 |
| 10-20 07:49 | +10 stop | XRP | DOWN | 0.67 | 0.52 | -1.84 |
| 10-20 07:48 | +10 stop | DOGE | UP | 0.55 | 0.40 | -1.85 |
| 10-20 07:48 | +10 stop | SOL | UP | 0.51 | 0.36 | -1.85 |
| 10-20 07:48 | +10 stop | NEAR | UP | 0.52 | 0.35 | -2.04 |
| 10-20 07:48 | +10 stop | ETH | UP | 0.60 | 0.37 | -2.64 |
| 10-20 07:48 | +10 stop | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-20 07:48 | +15 | HYPE | DOWN | 0.65 | 0.81 | 1.29 |
| 10-20 07:48 | +10 | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-20 07:48 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 10-20 07:48 | +5 | BNB | DOWN | 0.59 | 0.72 | 1.02 |
| 10-20 07:47 | +10 stop | ZEC | DOWN | 0.68 | 0.52 | -1.94 |
| 10-20 07:47 | +10 | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-20 07:47 | +5 | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-20 07:47 | +10 stop | XRP | DOWN | 0.68 | 0.52 | -1.94 |
| 10-20 07:47 | +10 | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-20 07:47 | +5 | XRP | DOWN | 0.68 | 0.77 | 0.61 |
| 10-20 07:47 | +10 stop | BNB | DOWN | 0.66 | 0.46 | -2.34 |
| 10-20 07:47 | +20 | BNB | DOWN | 0.66 | 0.95 | 2.71 |
