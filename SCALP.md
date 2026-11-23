# Range-Scalp Bot

*Updated Mon Nov 23 10:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69773 | 60882 | 8891 (146) | 0 | $-18786.55 | -4.3% |
| **+10¢** | 52071 | 41686 | 10385 (189) | 0 | $-17450.17 | -5.3% |
| **+15¢** | 43638 | 32451 | 11187 (244) | 0 | $-15586.46 | -5.7% |
| **+20¢** | 38857 | 27087 | 11770 (309) | 0 | $-13933.15 | -5.7% |
| **+10¢ (15¢ stop)** | 84965 | 84775 | 190 (118) | 0 | $-31203.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 09:57 | +10 stop | DOGE | DOWN | 0.66 | 0.40 | -2.93 |
| 11-23 09:57 | +20 | DOGE | DOWN | 0.69 | yes | -7.05 |
| 11-23 09:57 | +15 | DOGE | DOWN | 0.69 | yes | -7.05 |
| 11-23 09:57 | +10 | DOGE | DOWN | 0.70 | yes | -7.15 |
| 11-23 09:57 | +5 | DOGE | DOWN | 0.70 | yes | -7.15 |
| 11-23 09:57 | +10 stop | XRP | DOWN | 0.55 | 0.21 | -3.70 |
| 11-23 09:57 | +20 | XRP | DOWN | 0.55 | yes | -5.68 |
| 11-23 09:57 | +15 | XRP | DOWN | 0.56 | yes | -5.78 |
| 11-23 09:57 | +10 | XRP | DOWN | 0.56 | yes | -5.78 |
| 11-23 09:57 | +5 | XRP | DOWN | 0.56 | 0.62 | 0.25 |
| 11-23 09:56 | +10 stop | SOL | UP | 0.68 | 0.86 | 1.55 |
| 11-23 09:50 | +10 stop | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 11-23 09:48 | +10 stop | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-23 09:47 | +10 | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-23 09:47 | +10 stop | NEAR | DOWN | 0.69 | 0.82 | 1.01 |
| 11-23 09:47 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.29 |
| 11-23 09:47 | +5 | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-23 09:47 | +5 | XRP | DOWN | 0.60 | 0.67 | 0.37 |
| 11-23 09:47 | +5 | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-23 09:47 | +10 stop | SOL | UP | 0.57 | 0.40 | -2.05 |
| 11-23 09:47 | +20 | SOL | UP | 0.57 | 0.86 | 2.63 |
| 11-23 09:47 | +15 | SOL | UP | 0.57 | 0.75 | 1.48 |
| 11-23 09:47 | +10 | SOL | UP | 0.57 | 0.68 | 0.76 |
| 11-23 09:47 | +5 | SOL | UP | 0.57 | 0.68 | 0.76 |
| 11-23 09:47 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 11-23 09:46 | +10 stop | DOGE | DOWN | 0.59 | 0.75 | 1.29 |
| 11-23 09:46 | +20 | DOGE | DOWN | 0.59 | 0.79 | 1.71 |
| 11-23 09:46 | +15 | DOGE | DOWN | 0.59 | 0.75 | 1.29 |
| 11-23 09:46 | +10 | DOGE | DOWN | 0.59 | 0.75 | 1.29 |
| 11-23 09:46 | +5 | DOGE | DOWN | 0.59 | 0.66 | 0.37 |
| 11-23 09:46 | +10 stop | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 11-23 09:46 | +20 | BTC | DOWN | 0.54 | 0.75 | 1.78 |
| 11-23 09:46 | +15 | BTC | DOWN | 0.53 | 0.75 | 1.88 |
| 11-23 09:46 | +10 | BTC | DOWN | 0.53 | 0.63 | 0.65 |
| 11-23 09:46 | +5 | BTC | DOWN | 0.53 | 0.60 | 0.35 |
| 11-23 09:46 | +10 stop | XRP | DOWN | 0.55 | 0.67 | 0.86 |
| 11-23 09:46 | +20 | XRP | DOWN | 0.54 | 0.79 | 2.20 |
| 11-23 09:46 | +15 | XRP | DOWN | 0.54 | 0.79 | 2.20 |
| 11-23 09:46 | +10 | XRP | DOWN | 0.55 | 0.67 | 0.86 |
| 11-23 09:46 | +5 | XRP | DOWN | 0.55 | 0.62 | 0.35 |
