# Range-Scalp Bot

*Updated Thu Oct 15 03:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17030 | 14778 | 2252 (28) | 0 | $-5243.76 | -4.9% |
| **+10¢** | 12877 | 10266 | 2611 (40) | 2 | $-4768.13 | -5.9% |
| **+15¢** | 10811 | 8005 | 2806 (59) | 2 | $-4269.94 | -6.3% |
| **+20¢** | 9606 | 6668 | 2938 (76) | 2 | $-3748.07 | -6.2% |
| **+10¢ (15¢ stop)** | 20944 | 20894 | 50 (29) | 0 | $-8096.51 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 03:39 | +10 stop | ZEC | UP | 0.46 | 0.28 | -2.13 |
| 10-15 03:37 | +10 stop | DOGE | DOWN | 0.68 | 0.45 | -2.64 |
| 10-15 03:37 | +10 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-15 03:37 | +5 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-15 03:36 | +10 stop | BNB | DOWN | 0.67 | 0.40 | -3.03 |
| 10-15 03:36 | +10 | BNB | DOWN | 0.67 | 0.80 | 1.02 |
| 10-15 03:36 | +5 | BNB | DOWN | 0.67 | 0.80 | 1.02 |
| 10-15 03:36 | +10 stop | XRP | DOWN | 0.60 | 0.70 | 0.68 |
| 10-15 03:36 | +10 stop | ETH | DOWN | 0.69 | 0.49 | -2.33 |
| 10-15 03:36 | +10 | ETH | DOWN | 0.67 | 0.89 | 1.97 |
| 10-15 03:36 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
| 10-15 03:35 | +10 stop | SOL | DOWN | 0.71 | 0.42 | -3.23 |
| 10-15 03:35 | +10 | SOL | DOWN | 0.71 | open |  |
| 10-15 03:35 | +5 | SOL | DOWN | 0.66 | 0.71 | 0.19 |
| 10-15 03:34 | +10 stop | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-15 03:34 | +10 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-15 03:34 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-15 03:33 | +5 | ETH | DOWN | 0.62 | 0.68 | 0.27 |
| 10-15 03:33 | +10 stop | BNB | DOWN | 0.56 | 0.69 | 0.97 |
| 10-15 03:33 | +20 | BNB | DOWN | 0.56 | 0.80 | 2.10 |
| 10-15 03:33 | +15 | BNB | DOWN | 0.56 | 0.80 | 2.10 |
| 10-15 03:33 | +10 | BNB | DOWN | 0.56 | 0.69 | 0.97 |
| 10-15 03:33 | +5 | BNB | DOWN | 0.56 | 0.65 | 0.56 |
| 10-15 03:32 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-15 03:32 | +10 stop | SOL | DOWN | 0.57 | 0.68 | 0.76 |
| 10-15 03:32 | +20 | SOL | DOWN | 0.57 | 0.78 | 1.79 |
| 10-15 03:32 | +15 | SOL | DOWN | 0.57 | 0.76 | 1.59 |
| 10-15 03:32 | +10 | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 10-15 03:32 | +5 | SOL | DOWN | 0.58 | 0.64 | 0.25 |
| 10-15 03:31 | +10 stop | HYPE | DOWN | 0.65 | 0.80 | 1.18 |
| 10-15 03:31 | +20 | HYPE | DOWN | 0.66 | 0.89 | 2.03 |
| 10-15 03:31 | +15 | HYPE | DOWN | 0.67 | 0.85 | 1.51 |
| 10-15 03:31 | +10 | HYPE | DOWN | 0.68 | 0.80 | 0.95 |
| 10-15 03:31 | +5 | HYPE | DOWN | 0.69 | 0.74 | 0.22 |
| 10-15 03:31 | +10 stop | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-15 03:31 | +20 | DOGE | DOWN | 0.64 | open |  |
| 10-15 03:31 | +15 | DOGE | DOWN | 0.64 | open |  |
| 10-15 03:31 | +10 | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 10-15 03:31 | +5 | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 10-15 03:31 | +10 stop | ETH | DOWN | 0.57 | 0.68 | 0.76 |
