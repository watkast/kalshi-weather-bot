# Range-Scalp Bot

*Updated Wed Nov 25 06:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71536 | 62442 | 9094 (157) | 0 | $-19035.09 | -4.2% |
| **+10¢** | 53357 | 42732 | 10625 (203) | 0 | $-17664.07 | -5.3% |
| **+15¢** | 44687 | 33248 | 11439 (260) | 0 | $-15706.03 | -5.6% |
| **+20¢** | 39787 | 27738 | 12049 (326) | 1 | $-14127.67 | -5.7% |
| **+10¢ (15¢ stop)** | 87099 | 86896 | 203 (123) | 0 | $-32010.77 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 06:19 | +10 stop | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 11-25 06:19 | +10 | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 11-25 06:19 | +5 | BNB | DOWN | 0.68 | 0.74 | 0.30 |
| 11-25 06:19 | +10 stop | ZEC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-25 06:19 | +10 stop | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 11-25 06:19 | +20 | XRP | DOWN | 0.71 | 0.93 | 1.97 |
| 11-25 06:19 | +15 | XRP | DOWN | 0.71 | 0.87 | 1.37 |
| 11-25 06:19 | +10 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 11-25 06:19 | +5 | XRP | DOWN | 0.71 | 0.78 | 0.42 |
| 11-25 06:18 | +10 stop | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 11-25 06:18 | +10 | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 11-25 06:18 | +5 | ETH | DOWN | 0.64 | 0.70 | 0.28 |
| 11-25 06:18 | +10 stop | BTC | DOWN | 0.61 | 0.75 | 1.09 |
| 11-25 06:18 | +10 | BTC | DOWN | 0.61 | 0.75 | 1.09 |
| 11-25 06:17 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
| 11-25 06:17 | +5 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-25 06:17 | +10 stop | NEAR | DOWN | 0.54 | 0.65 | 0.76 |
| 11-25 06:17 | +20 | NEAR | DOWN | 0.54 | 0.78 | 2.09 |
| 11-25 06:17 | +15 | NEAR | DOWN | 0.54 | 0.78 | 2.09 |
| 11-25 06:17 | +10 | NEAR | DOWN | 0.54 | 0.65 | 0.76 |
| 11-25 06:17 | +5 | NEAR | DOWN | 0.54 | 0.61 | 0.35 |
| 11-25 06:17 | +10 stop | DOGE | DOWN | 0.71 | 0.83 | 0.96 |
| 11-25 06:17 | +20 | DOGE | DOWN | 0.71 | open |  |
| 11-25 06:17 | +15 | DOGE | DOWN | 0.71 | 0.89 | 1.62 |
| 11-25 06:17 | +10 | DOGE | DOWN | 0.71 | 0.83 | 0.99 |
| 11-25 06:17 | +5 | DOGE | DOWN | 0.71 | 0.77 | 0.36 |
| 11-25 06:16 | +10 stop | HYPE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-25 06:16 | +20 | HYPE | DOWN | 0.67 | 0.88 | 1.86 |
| 11-25 06:16 | +15 | HYPE | DOWN | 0.67 | 0.84 | 1.44 |
| 11-25 06:16 | +10 | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-25 06:16 | +5 | HYPE | DOWN | 0.68 | 0.74 | 0.30 |
| 11-25 06:16 | +10 stop | ZEC | DOWN | 0.67 | 0.52 | -1.84 |
| 11-25 06:16 | +20 | ZEC | DOWN | 0.67 | 0.87 | 1.76 |
| 11-25 06:16 | +15 | ZEC | DOWN | 0.67 | 0.83 | 1.34 |
| 11-25 06:16 | +10 | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-25 06:16 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-25 06:16 | +10 stop | BNB | DOWN | 0.61 | 0.72 | 0.78 |
| 11-25 06:16 | +20 | BNB | DOWN | 0.61 | 0.83 | 1.93 |
| 11-25 06:16 | +15 | BNB | DOWN | 0.61 | 0.79 | 1.51 |
| 11-25 06:16 | +10 | BNB | DOWN | 0.61 | 0.72 | 0.78 |
