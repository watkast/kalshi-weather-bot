# Range-Scalp Bot

*Updated Wed Nov 18 08:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63867 | 55706 | 8161 (119) | 3 | $-17434.37 | -4.3% |
| **+10¢** | 47715 | 38163 | 9552 (160) | 5 | $-16342.35 | -5.4% |
| **+15¢** | 40008 | 29709 | 10299 (205) | 5 | $-14806.46 | -5.9% |
| **+20¢** | 35631 | 24820 | 10811 (260) | 6 | $-13096.65 | -5.9% |
| **+10¢ (15¢ stop)** | 77703 | 77545 | 158 (93) | 1 | $-28525.60 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 08:40 | +10 stop | ZEC | UP | 0.63 | open |  |
| 11-18 08:39 | +10 stop | ZEC | DOWN | 0.69 | 0.42 | -3.03 |
| 11-18 08:39 | +5 | ZEC | DOWN | 0.69 | open |  |
| 11-18 08:38 | +10 stop | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 11-18 08:38 | +15 | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 11-18 08:38 | +10 | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 11-18 08:38 | +5 | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 11-18 08:38 | +10 stop | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-18 08:38 | +5 | DOGE | DOWN | 0.70 | 0.76 | 0.32 |
| 11-18 08:37 | +10 stop | SOL | DOWN | 0.69 | 0.86 | 1.46 |
| 11-18 08:37 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 11-18 08:37 | +5 | BNB | DOWN | 0.59 | 0.75 | 1.29 |
| 11-18 08:37 | +10 stop | XRP | DOWN | 0.57 | 0.73 | 1.28 |
| 11-18 08:37 | +20 | XRP | DOWN | 0.57 | 0.80 | 2.00 |
| 11-18 08:37 | +10 | XRP | DOWN | 0.57 | 0.73 | 1.28 |
| 11-18 08:37 | +5 | XRP | DOWN | 0.57 | 0.73 | 1.28 |
| 11-18 08:37 | +10 stop | ETH | DOWN | 0.58 | 0.78 | 1.69 |
| 11-18 08:37 | +10 stop | DOGE | DOWN | 0.50 | 0.62 | 0.85 |
| 11-18 08:37 | +5 | DOGE | DOWN | 0.50 | 0.62 | 0.85 |
| 11-18 08:37 | +10 | BNB | DOWN | 0.58 | 0.75 | 1.38 |
| 11-18 08:37 | +5 | BNB | DOWN | 0.58 | 0.65 | 0.36 |
| 11-18 08:36 | +10 stop | ZEC | DOWN | 0.57 | 0.73 | 1.28 |
| 11-18 08:35 | +10 stop | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-18 08:34 | +10 stop | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 11-18 08:34 | +10 stop | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 11-18 08:34 | +5 | DOGE | DOWN | 0.64 | 0.70 | 0.28 |
| 11-18 08:33 | +5 | HYPE | UP | 0.71 | 0.76 | 0.22 |
| 11-18 08:33 | +10 stop | BNB | DOWN | 0.56 | 0.66 | 0.66 |
| 11-18 08:33 | +10 stop | ZEC | UP | 0.58 | 0.42 | -1.96 |
| 11-18 08:33 | +10 stop | XRP | DOWN | 0.68 | 0.82 | 1.13 |
| 11-18 08:33 | +15 | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 11-18 08:33 | +10 | XRP | DOWN | 0.68 | 0.82 | 1.13 |
| 11-18 08:33 | +5 | XRP | DOWN | 0.68 | 0.74 | 0.30 |
| 11-18 08:33 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 11-18 08:33 | +5 | DOGE | DOWN | 0.58 | 0.63 | 0.15 |
| 11-18 08:32 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-18 08:32 | +10 stop | BTC | DOWN | 0.51 | 0.63 | 0.85 |
| 11-18 08:32 | +10 stop | ETH | DOWN | 0.51 | 0.62 | 0.75 |
| 11-18 08:32 | +5 | SOL | DOWN | 0.65 | 0.71 | 0.29 |
| 11-18 08:32 | +10 stop | ZEC | DOWN | 0.64 | 0.45 | -2.25 |
