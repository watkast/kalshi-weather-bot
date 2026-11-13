# Range-Scalp Bot

*Updated Fri Nov 13 02:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57636 | 50265 | 7371 (101) | 0 | $-15726.44 | -4.3% |
| **+10¢** | 43076 | 34469 | 8607 (133) | 0 | $-14656.61 | -5.4% |
| **+15¢** | 36115 | 26851 | 9264 (167) | 0 | $-13213.82 | -5.8% |
| **+20¢** | 32177 | 22457 | 9720 (217) | 0 | $-11561.65 | -5.7% |
| **+10¢ (15¢ stop)** | 70272 | 70144 | 128 (78) | 0 | $-25883.75 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 02:09 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-13 02:09 | +20 | ZEC | DOWN | 0.67 | 0.94 | 2.52 |
| 11-13 02:09 | +15 | ZEC | DOWN | 0.69 | 0.84 | 1.29 |
| 11-13 02:09 | +10 | ZEC | DOWN | 0.65 | 0.79 | 1.12 |
| 11-13 02:09 | +5 | ZEC | DOWN | 0.65 | 0.79 | 1.12 |
| 11-13 02:02 | +5 | ETH | DOWN | 0.67 | 0.74 | 0.40 |
| 11-13 02:02 | +10 stop | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 11-13 02:02 | +20 | NEAR | DOWN | 0.68 | 0.88 | 1.76 |
| 11-13 02:02 | +15 | NEAR | DOWN | 0.68 | 0.84 | 1.34 |
| 11-13 02:02 | +10 | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 11-13 02:02 | +5 | NEAR | DOWN | 0.68 | 0.76 | 0.51 |
| 11-13 02:01 | +10 stop | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 11-13 02:01 | +20 | ETH | DOWN | 0.60 | 0.85 | 2.24 |
| 11-13 02:01 | +15 | ETH | DOWN | 0.61 | 0.78 | 1.40 |
| 11-13 02:01 | +10 | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 11-13 02:01 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 11-13 02:01 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-13 02:01 | +20 | BTC | DOWN | 0.66 | 0.88 | 1.96 |
| 11-13 02:01 | +15 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-13 02:01 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-13 02:01 | +5 | BTC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-13 02:01 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-13 02:01 | +20 | DOGE | DOWN | 0.65 | 0.85 | 1.75 |
| 11-13 02:01 | +15 | DOGE | DOWN | 0.64 | 0.82 | 1.52 |
| 11-13 02:01 | +10 | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 11-13 02:01 | +5 | DOGE | DOWN | 0.64 | 0.71 | 0.38 |
| 11-13 02:00 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-13 02:00 | +20 | ZEC | DOWN | 0.65 | 0.86 | 1.85 |
| 11-13 02:00 | +15 | ZEC | DOWN | 0.66 | 0.81 | 1.26 |
| 11-13 02:00 | +10 | ZEC | DOWN | 0.67 | 0.78 | 0.80 |
| 11-13 02:00 | +5 | ZEC | DOWN | 0.65 | 0.72 | 0.39 |
| 11-13 02:00 | +10 stop | XRP | DOWN | 0.63 | 0.76 | 1.00 |
| 11-13 02:00 | +20 | XRP | DOWN | 0.63 | 0.85 | 1.94 |
| 11-13 02:00 | +15 | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 11-13 02:00 | +10 | XRP | DOWN | 0.63 | 0.76 | 1.00 |
| 11-13 02:00 | +5 | XRP | DOWN | 0.63 | 0.76 | 1.00 |
| 11-13 01:56 | +5 | HYPE | DOWN | 0.59 | yes | -6.07 |
| 11-13 01:56 | +10 stop | BTC | DOWN | 0.63 | 0.43 | -2.35 |
| 11-13 01:56 | +10 stop | ZEC | DOWN | 0.50 | 0.65 | 1.16 |
| 11-13 01:56 | +10 | ZEC | DOWN | 0.50 | 0.65 | 1.16 |
