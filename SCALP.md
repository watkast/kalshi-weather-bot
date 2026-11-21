# Range-Scalp Bot

*Updated Sat Nov 21 08:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67281 | 58730 | 8551 (129) | 0 | $-18002.91 | -4.3% |
| **+10¢** | 50243 | 40249 | 9994 (171) | 0 | $-16711.97 | -5.3% |
| **+15¢** | 42138 | 31363 | 10775 (219) | 1 | $-14979.97 | -5.7% |
| **+20¢** | 37503 | 26180 | 11323 (276) | 1 | $-13310.33 | -5.7% |
| **+10¢ (15¢ stop)** | 81910 | 81744 | 166 (100) | 0 | $-30116.66 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 08:07 | +10 stop | XRP | DOWN | 0.64 | 0.77 | 1.00 |
| 11-21 08:06 | +10 stop | ETH | DOWN | 0.68 | 0.87 | 1.66 |
| 11-21 08:06 | +10 | ETH | DOWN | 0.69 | 0.87 | 1.57 |
| 11-21 08:06 | +5 | ETH | DOWN | 0.69 | 0.77 | 0.52 |
| 11-21 08:06 | +10 stop | BNB | DOWN | 0.62 | 0.79 | 1.41 |
| 11-21 08:06 | +15 | BNB | DOWN | 0.62 | 0.79 | 1.41 |
| 11-21 08:06 | +10 | BNB | DOWN | 0.62 | 0.79 | 1.41 |
| 11-21 08:06 | +5 | BNB | DOWN | 0.62 | 0.68 | 0.27 |
| 11-21 08:05 | +5 | ZEC | DOWN | 0.63 | 0.73 | 0.66 |
| 11-21 08:05 | +10 stop | NEAR | DOWN | 0.66 | 0.80 | 1.12 |
| 11-21 08:05 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 11-21 08:05 | +15 | NEAR | DOWN | 0.68 | 0.87 | 1.66 |
| 11-21 08:05 | +10 | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 11-21 08:05 | +5 | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 11-21 08:05 | +5 | DOGE | DOWN | 0.64 | 0.71 | 0.38 |
| 11-21 08:04 | +10 stop | HYPE | DOWN | 0.62 | 0.77 | 1.20 |
| 11-21 08:04 | +15 | HYPE | DOWN | 0.62 | 0.77 | 1.20 |
| 11-21 08:04 | +10 | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-21 08:04 | +5 | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-21 08:04 | +10 stop | XRP | DOWN | 0.69 | 0.52 | -2.03 |
| 11-21 08:04 | +15 | XRP | DOWN | 0.69 | open |  |
| 11-21 08:04 | +10 | XRP | DOWN | 0.69 | 0.83 | 1.15 |
| 11-21 08:04 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 11-21 08:04 | +10 stop | DOGE | DOWN | 0.67 | 0.80 | 1.02 |
| 11-21 08:04 | +15 | DOGE | DOWN | 0.68 | 0.83 | 1.24 |
| 11-21 08:04 | +10 | DOGE | DOWN | 0.68 | 0.80 | 0.92 |
| 11-21 08:04 | +5 | DOGE | DOWN | 0.68 | 0.75 | 0.40 |
| 11-21 08:04 | +10 stop | ZEC | DOWN | 0.63 | 0.84 | 1.83 |
| 11-21 08:04 | +15 | ZEC | DOWN | 0.64 | 0.84 | 1.73 |
| 11-21 08:04 | +10 | ZEC | DOWN | 0.64 | 0.84 | 1.73 |
| 11-21 08:04 | +5 | ZEC | DOWN | 0.64 | 0.72 | 0.48 |
| 11-21 08:01 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-21 08:01 | +20 | BTC | DOWN | 0.69 | 0.91 | 1.96 |
| 11-21 08:01 | +15 | BTC | DOWN | 0.69 | 0.85 | 1.36 |
| 11-21 08:01 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-21 08:01 | +5 | BTC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-21 08:01 | +10 stop | ZEC | DOWN | 0.58 | 0.72 | 1.07 |
| 11-21 08:01 | +20 | ZEC | DOWN | 0.57 | 0.84 | 2.42 |
| 11-21 08:01 | +15 | ZEC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-21 08:01 | +10 | ZEC | DOWN | 0.57 | 0.72 | 1.17 |
