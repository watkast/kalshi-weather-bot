# Range-Scalp Bot

*Updated Wed Nov 18 07:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63810 | 55651 | 8159 (119) | 0 | $-17450.80 | -4.3% |
| **+10¢** | 47681 | 38131 | 9550 (160) | 0 | $-16370.92 | -5.5% |
| **+15¢** | 39976 | 29679 | 10297 (205) | 0 | $-14844.15 | -5.9% |
| **+20¢** | 35603 | 24794 | 10809 (260) | 0 | $-13135.15 | -5.9% |
| **+10¢ (15¢ stop)** | 77633 | 77475 | 158 (93) | 0 | $-28520.47 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 07:32 | +10 stop | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 11-18 07:31 | +10 stop | BTC | DOWN | 0.63 | 0.77 | 1.10 |
| 11-18 07:31 | +20 | BTC | DOWN | 0.63 | 0.86 | 2.04 |
| 11-18 07:31 | +15 | BTC | DOWN | 0.63 | 0.82 | 1.62 |
| 11-18 07:31 | +10 | BTC | DOWN | 0.63 | 0.77 | 1.10 |
| 11-18 07:31 | +5 | BTC | DOWN | 0.63 | 0.69 | 0.28 |
| 11-18 07:31 | +10 stop | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 11-18 07:31 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.91 |
| 11-18 07:31 | +15 | ETH | DOWN | 0.71 | 0.87 | 1.37 |
| 11-18 07:31 | +10 | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 11-18 07:31 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
| 11-18 07:31 | +10 stop | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-18 07:31 | +20 | ZEC | DOWN | 0.64 | 0.84 | 1.73 |
| 11-18 07:31 | +15 | ZEC | DOWN | 0.64 | 0.79 | 1.21 |
| 11-18 07:31 | +10 | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-18 07:31 | +5 | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-18 07:31 | +10 stop | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 11-18 07:31 | +20 | BNB | DOWN | 0.66 | 0.92 | 2.39 |
| 11-18 07:31 | +15 | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 11-18 07:31 | +10 | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 11-18 07:31 | +5 | BNB | DOWN | 0.66 | 0.73 | 0.40 |
| 11-18 07:31 | +10 stop | HYPE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-18 07:31 | +20 | HYPE | DOWN | 0.69 | 0.90 | 1.87 |
| 11-18 07:31 | +15 | HYPE | DOWN | 0.69 | 0.88 | 1.62 |
| 11-18 07:31 | +10 | HYPE | DOWN | 0.69 | 0.83 | 1.10 |
| 11-18 07:31 | +5 | HYPE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-18 07:31 | +10 stop | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 11-18 07:31 | +20 | NEAR | DOWN | 0.64 | 0.86 | 1.94 |
| 11-18 07:31 | +15 | NEAR | DOWN | 0.64 | 0.82 | 1.52 |
| 11-18 07:31 | +10 | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 11-18 07:31 | +5 | NEAR | DOWN | 0.64 | 0.70 | 0.24 |
| 11-18 07:31 | +10 stop | DOGE | DOWN | 0.67 | 0.86 | 1.65 |
| 11-18 07:31 | +20 | DOGE | DOWN | 0.67 | 0.87 | 1.76 |
| 11-18 07:31 | +15 | DOGE | DOWN | 0.67 | 0.86 | 1.65 |
| 11-18 07:31 | +10 | DOGE | DOWN | 0.67 | 0.86 | 1.65 |
| 11-18 07:31 | +5 | DOGE | DOWN | 0.67 | 0.75 | 0.50 |
| 11-18 07:31 | +10 stop | XRP | DOWN | 0.58 | 0.68 | 0.68 |
| 11-18 07:31 | +20 | XRP | DOWN | 0.64 | 0.84 | 1.77 |
| 11-18 07:31 | +15 | XRP | DOWN | 0.64 | 0.83 | 1.63 |
| 11-18 07:31 | +10 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
