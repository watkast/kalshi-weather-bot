# Range-Scalp Bot

*Updated Fri Oct 30 02:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40114 | 35041 | 5073 (51) | 0 | $-10994.82 | -4.4% |
| **+10¢** | 29887 | 24016 | 5871 (74) | 0 | $-9750.09 | -5.2% |
| **+15¢** | 25000 | 18683 | 6317 (101) | 0 | $-8728.92 | -5.6% |
| **+20¢** | 22183 | 15559 | 6624 (130) | 0 | $-7652.90 | -5.5% |
| **+10¢ (15¢ stop)** | 48924 | 48854 | 70 (37) | 0 | $-18492.32 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 02:50 | +10 stop | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 02:50 | +10 | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 02:50 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 10-30 02:49 | +5 | NEAR | DOWN | 0.59 | 0.67 | 0.47 |
| 10-30 02:48 | +5 | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-30 02:47 | +5 | BNB | DOWN | 0.66 | 0.74 | 0.50 |
| 10-30 02:47 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.19 |
| 10-30 02:47 | +10 stop | XRP | DOWN | 0.60 | 0.70 | 0.68 |
| 10-30 02:47 | +20 | XRP | DOWN | 0.60 | 0.80 | 1.71 |
| 10-30 02:47 | +15 | XRP | DOWN | 0.60 | 0.76 | 1.30 |
| 10-30 02:47 | +10 | XRP | DOWN | 0.60 | 0.70 | 0.68 |
| 10-30 02:47 | +5 | XRP | DOWN | 0.60 | 0.70 | 0.68 |
| 10-30 02:47 | +5 | BTC | DOWN | 0.67 | 0.76 | 0.61 |
| 10-30 02:46 | +10 stop | ZEC | DOWN | 0.62 | 0.76 | 1.10 |
| 10-30 02:46 | +20 | ZEC | DOWN | 0.62 | 0.82 | 1.72 |
| 10-30 02:46 | +15 | ZEC | DOWN | 0.62 | 0.77 | 1.20 |
| 10-30 02:46 | +10 | ZEC | DOWN | 0.62 | 0.76 | 1.10 |
| 10-30 02:46 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.17 |
| 10-30 02:46 | +10 stop | ETH | DOWN | 0.63 | 0.75 | 0.89 |
| 10-30 02:46 | +20 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
| 10-30 02:46 | +15 | ETH | DOWN | 0.64 | 0.79 | 1.21 |
| 10-30 02:46 | +10 | ETH | DOWN | 0.64 | 0.75 | 0.79 |
| 10-30 02:46 | +5 | ETH | DOWN | 0.64 | 0.71 | 0.38 |
| 10-30 02:46 | +10 stop | BTC | DOWN | 0.62 | 0.76 | 1.10 |
| 10-30 02:46 | +20 | BTC | DOWN | 0.62 | 0.86 | 2.14 |
| 10-30 02:46 | +15 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-30 02:46 | +10 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-30 02:46 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-30 02:46 | +10 stop | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 10-30 02:46 | +20 | SOL | DOWN | 0.66 | 0.86 | 1.75 |
| 10-30 02:46 | +15 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 10-30 02:46 | +10 | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 10-30 02:46 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.29 |
| 10-30 02:46 | +10 stop | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 10-30 02:46 | +20 | BNB | DOWN | 0.62 | 0.86 | 2.14 |
| 10-30 02:46 | +15 | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 10-30 02:46 | +10 | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 10-30 02:46 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 10-30 02:46 | +10 stop | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 10-30 02:46 | +20 | DOGE | DOWN | 0.62 | 0.82 | 1.72 |
