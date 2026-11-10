# Range-Scalp Bot

*Updated Tue Nov 10 16:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54760 | 47765 | 6995 (91) | 0 | $-14919.92 | -4.3% |
| **+10¢** | 40922 | 32760 | 8162 (121) | 0 | $-13843.16 | -5.4% |
| **+15¢** | 34303 | 25505 | 8798 (155) | 0 | $-12590.21 | -5.9% |
| **+20¢** | 30541 | 21309 | 9232 (204) | 0 | $-11019.98 | -5.8% |
| **+10¢ (15¢ stop)** | 66703 | 66589 | 114 (70) | 0 | $-24663.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 16:54 | +10 stop | ETH | DOWN | 0.55 | 0.71 | 1.27 |
| 11-10 16:54 | +10 | ETH | DOWN | 0.55 | 0.71 | 1.27 |
| 11-10 16:54 | +5 | ETH | DOWN | 0.55 | 0.71 | 1.27 |
| 11-10 16:53 | +10 stop | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 11-10 16:53 | +15 | NEAR | DOWN | 0.70 | 0.85 | 1.26 |
| 11-10 16:53 | +10 | NEAR | DOWN | 0.71 | 0.85 | 1.16 |
| 11-10 16:53 | +5 | NEAR | DOWN | 0.71 | 0.85 | 1.16 |
| 11-10 16:53 | +10 stop | SOL | DOWN | 0.68 | 0.82 | 1.17 |
| 11-10 16:53 | +20 | SOL | DOWN | 0.67 | 0.88 | 1.91 |
| 11-10 16:53 | +15 | SOL | DOWN | 0.64 | 0.82 | 1.52 |
| 11-10 16:53 | +10 | SOL | DOWN | 0.64 | 0.82 | 1.52 |
| 11-10 16:53 | +5 | SOL | DOWN | 0.65 | 0.82 | 1.43 |
| 11-10 16:53 | +15 | ETH | DOWN | 0.50 | 0.71 | 1.77 |
| 11-10 16:53 | +10 | ETH | DOWN | 0.50 | 0.63 | 0.95 |
| 11-10 16:53 | +5 | ETH | DOWN | 0.50 | 0.63 | 0.95 |
| 11-10 16:49 | +10 | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 11-10 16:49 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 11-10 16:49 | +10 stop | ETH | DOWN | 0.70 | 0.50 | -2.33 |
| 11-10 16:47 | +10 stop | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 11-10 16:47 | +20 | ZEC | DOWN | 0.62 | 0.83 | 1.83 |
| 11-10 16:47 | +15 | ZEC | DOWN | 0.62 | 0.83 | 1.83 |
| 11-10 16:47 | +10 | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 11-10 16:47 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.17 |
| 11-10 16:46 | +10 stop | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-10 16:46 | +20 | DOGE | DOWN | 0.65 | 0.85 | 1.75 |
| 11-10 16:46 | +15 | DOGE | DOWN | 0.65 | 0.82 | 1.43 |
| 11-10 16:46 | +10 | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-10 16:46 | +5 | DOGE | DOWN | 0.65 | 0.73 | 0.50 |
| 11-10 16:46 | +10 stop | ETH | DOWN | 0.60 | 0.71 | 0.80 |
| 11-10 16:46 | +20 | ETH | DOWN | 0.60 | 0.86 | 2.38 |
| 11-10 16:46 | +15 | ETH | DOWN | 0.60 | 0.78 | 1.54 |
| 11-10 16:46 | +10 | ETH | DOWN | 0.60 | 0.71 | 0.77 |
| 11-10 16:46 | +5 | ETH | DOWN | 0.60 | 0.67 | 0.36 |
| 11-10 16:46 | +10 stop | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 11-10 16:46 | +20 | BNB | DOWN | 0.70 | 0.93 | 2.06 |
| 11-10 16:46 | +15 | BNB | DOWN | 0.70 | 0.87 | 1.47 |
| 11-10 16:46 | +10 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 11-10 16:46 | +5 | BNB | DOWN | 0.71 | 0.76 | 0.22 |
| 11-10 16:45 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.90 |
| 11-10 16:45 | +20 | HYPE | DOWN | 0.68 | 0.90 | 1.99 |
