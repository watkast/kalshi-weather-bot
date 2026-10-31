# Range-Scalp Bot

*Updated Sat Oct 31 03:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41719 | 36405 | 5314 (54) | 0 | $-11693.78 | -4.5% |
| **+10¢** | 31096 | 24947 | 6149 (78) | 0 | $-10431.04 | -5.3% |
| **+15¢** | 25989 | 19359 | 6630 (106) | 0 | $-9525.73 | -5.8% |
| **+20¢** | 23072 | 16128 | 6944 (137) | 0 | $-8395.18 | -5.8% |
| **+10¢ (15¢ stop)** | 50842 | 50767 | 75 (41) | 0 | $-19185.22 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 03:32 | +10 stop | BNB | DOWN | 0.68 | 0.80 | 0.92 |
| 10-31 03:32 | +20 | BNB | DOWN | 0.68 | 0.89 | 1.87 |
| 10-31 03:32 | +15 | BNB | DOWN | 0.68 | 0.84 | 1.34 |
| 10-31 03:32 | +10 | BNB | DOWN | 0.68 | 0.80 | 0.92 |
| 10-31 03:32 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.51 |
| 10-31 03:32 | +5 | ETH | DOWN | 0.66 | 0.86 | 1.75 |
| 10-31 03:32 | +5 | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-31 03:32 | +5 | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-31 03:31 | +10 stop | ETH | DOWN | 0.61 | 0.86 | 2.24 |
| 10-31 03:31 | +20 | ETH | DOWN | 0.61 | 0.86 | 2.24 |
| 10-31 03:31 | +15 | ETH | DOWN | 0.61 | 0.86 | 2.24 |
| 10-31 03:31 | +10 | ETH | DOWN | 0.61 | 0.86 | 2.24 |
| 10-31 03:31 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 10-31 03:31 | +10 stop | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-31 03:31 | +20 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 10-31 03:31 | +15 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-31 03:31 | +10 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-31 03:31 | +5 | DOGE | DOWN | 0.64 | 0.71 | 0.38 |
| 10-31 03:31 | +10 stop | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 10-31 03:31 | +20 | NEAR | DOWN | 0.71 | 0.92 | 1.84 |
| 10-31 03:31 | +15 | NEAR | DOWN | 0.71 | 0.87 | 1.37 |
| 10-31 03:31 | +10 | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 10-31 03:31 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 10-31 03:31 | +10 stop | BTC | DOWN | 0.62 | 0.82 | 1.72 |
| 10-31 03:31 | +20 | BTC | DOWN | 0.62 | 0.82 | 1.72 |
| 10-31 03:31 | +15 | BTC | DOWN | 0.62 | 0.82 | 1.72 |
| 10-31 03:31 | +10 | BTC | DOWN | 0.62 | 0.82 | 1.72 |
| 10-31 03:31 | +5 | BTC | DOWN | 0.62 | 0.68 | 0.27 |
| 10-31 03:29 | +10 stop | XRP | DOWN | 0.49 | 0.64 | 1.15 |
| 10-31 03:29 | +20 | XRP | DOWN | 0.50 | 0.84 | 3.12 |
| 10-31 03:29 | +15 | XRP | DOWN | 0.51 | 0.84 | 3.02 |
| 10-31 03:29 | +10 | XRP | DOWN | 0.53 | 0.64 | 0.76 |
| 10-31 03:29 | +5 | XRP | DOWN | 0.51 | 0.64 | 0.95 |
| 10-31 03:22 | +10 stop | DOGE | UP | 0.64 | 0.74 | 0.69 |
| 10-31 03:22 | +5 | DOGE | UP | 0.64 | 0.72 | 0.48 |
| 10-31 03:22 | +10 stop | XRP | UP | 0.62 | 0.73 | 0.79 |
| 10-31 03:22 | +10 | XRP | UP | 0.63 | 0.73 | 0.70 |
| 10-31 03:21 | +10 stop | BNB | UP | 0.58 | 0.70 | 0.87 |
| 10-31 03:21 | +5 | HYPE | UP | 0.71 | 0.78 | 0.42 |
| 10-31 03:19 | +10 stop | HYPE | UP | 0.55 | 0.69 | 1.07 |
