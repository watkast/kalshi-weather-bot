# Range-Scalp Bot

*Updated Fri Nov 13 03:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57780 | 50402 | 7378 (101) | 3 | $-15696.66 | -4.3% |
| **+10¢** | 43175 | 34559 | 8616 (133) | 4 | $-14621.75 | -5.4% |
| **+15¢** | 36196 | 26924 | 9272 (167) | 4 | $-13147.37 | -5.8% |
| **+20¢** | 32244 | 22514 | 9730 (217) | 4 | $-11513.04 | -5.7% |
| **+10¢ (15¢ stop)** | 70433 | 70305 | 128 (78) | 0 | $-25948.20 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 03:54 | +10 stop | ZEC | DOWN | 0.70 | 0.55 | -1.83 |
| 11-13 03:51 | +10 stop | ZEC | DOWN | 0.68 | 0.53 | -1.84 |
| 11-13 03:50 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-13 03:50 | +10 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-13 03:49 | +10 stop | HYPE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-13 03:49 | +10 | HYPE | DOWN | 0.69 | 0.87 | 1.57 |
| 11-13 03:49 | +5 | HYPE | DOWN | 0.69 | 0.76 | 0.42 |
| 11-13 03:48 | +10 | HYPE | DOWN | 0.54 | 0.64 | 0.65 |
| 11-13 03:48 | +5 | HYPE | DOWN | 0.54 | 0.64 | 0.65 |
| 11-13 03:48 | +10 stop | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
| 11-13 03:48 | +10 stop | ETH | DOWN | 0.68 | 0.86 | 1.55 |
| 11-13 03:48 | +15 | ETH | DOWN | 0.68 | 0.86 | 1.55 |
| 11-13 03:48 | +10 | ETH | DOWN | 0.68 | 0.86 | 1.55 |
| 11-13 03:48 | +5 | ETH | DOWN | 0.68 | 0.75 | 0.40 |
| 11-13 03:48 | +5 | SOL | DOWN | 0.69 | 0.78 | 0.62 |
| 11-13 03:48 | +5 | BNB | DOWN | 0.61 | 0.68 | 0.37 |
| 11-13 03:48 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
| 11-13 03:47 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 11-13 03:47 | +10 stop | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 11-13 03:47 | +10 stop | BTC | DOWN | 0.61 | 0.72 | 0.78 |
| 11-13 03:46 | +10 stop | HYPE | DOWN | 0.55 | 0.68 | 0.96 |
| 11-13 03:46 | +20 | HYPE | DOWN | 0.55 | 0.76 | 1.79 |
| 11-13 03:46 | +15 | HYPE | DOWN | 0.54 | 0.69 | 1.17 |
| 11-13 03:46 | +10 | HYPE | DOWN | 0.54 | 0.64 | 0.65 |
| 11-13 03:46 | +5 | HYPE | DOWN | 0.54 | 0.64 | 0.65 |
| 11-13 03:46 | +10 stop | SOL | DOWN | 0.59 | 0.69 | 0.68 |
| 11-13 03:46 | +20 | SOL | DOWN | 0.59 | 0.81 | 1.92 |
| 11-13 03:46 | +15 | SOL | DOWN | 0.58 | 0.78 | 1.69 |
| 11-13 03:46 | +10 | SOL | DOWN | 0.58 | 0.68 | 0.70 |
| 11-13 03:46 | +5 | SOL | DOWN | 0.58 | 0.66 | 0.50 |
| 11-13 03:46 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 11-13 03:46 | +20 | BNB | DOWN | 0.58 | 0.79 | 1.80 |
| 11-13 03:46 | +15 | BNB | DOWN | 0.58 | 0.75 | 1.38 |
| 11-13 03:46 | +10 | BNB | DOWN | 0.58 | 0.68 | 0.69 |
| 11-13 03:46 | +5 | BNB | DOWN | 0.55 | 0.63 | 0.45 |
| 11-13 03:46 | +10 stop | DOGE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-13 03:46 | +20 | DOGE | DOWN | 0.58 | 0.83 | 2.19 |
| 11-13 03:46 | +15 | DOGE | DOWN | 0.59 | 0.74 | 1.21 |
| 11-13 03:46 | +10 | DOGE | DOWN | 0.58 | 0.69 | 0.73 |
| 11-13 03:46 | +5 | DOGE | DOWN | 0.58 | 0.65 | 0.32 |
