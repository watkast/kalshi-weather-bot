# Range-Scalp Bot

*Updated Fri Oct 23 22:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31075 | 27079 | 3996 (40) | 0 | $-8985.78 | -4.6% |
| **+10¢** | 23243 | 18627 | 4616 (58) | 0 | $-7985.88 | -5.5% |
| **+15¢** | 19447 | 14481 | 4966 (81) | 0 | $-7187.73 | -5.9% |
| **+20¢** | 17225 | 12024 | 5201 (103) | 0 | $-6434.82 | -5.9% |
| **+10¢ (15¢ stop)** | 38128 | 38069 | 59 (32) | 0 | $-14601.01 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 22:46 | +10 stop | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 10-23 22:46 | +20 | ETH | DOWN | 0.60 | 0.94 | 3.15 |
| 10-23 22:46 | +15 | ETH | DOWN | 0.60 | 0.76 | 1.30 |
| 10-23 22:46 | +10 | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 10-23 22:46 | +5 | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 10-23 22:46 | +10 stop | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-23 22:46 | +20 | BNB | DOWN | 0.61 | 0.87 | 2.35 |
| 10-23 22:46 | +15 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-23 22:46 | +10 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-23 22:46 | +5 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-23 22:46 | +10 stop | NEAR | DOWN | 0.64 | 0.76 | 0.89 |
| 10-23 22:46 | +20 | NEAR | DOWN | 0.64 | 0.88 | 2.14 |
| 10-23 22:46 | +15 | NEAR | DOWN | 0.64 | 0.83 | 1.62 |
| 10-23 22:46 | +10 | NEAR | DOWN | 0.64 | 0.76 | 0.89 |
| 10-23 22:46 | +5 | NEAR | DOWN | 0.64 | 0.72 | 0.47 |
| 10-23 22:46 | +10 stop | SOL | DOWN | 0.66 | 0.82 | 1.33 |
| 10-23 22:46 | +20 | SOL | DOWN | 0.66 | 0.92 | 2.39 |
| 10-23 22:46 | +15 | SOL | DOWN | 0.66 | 0.82 | 1.33 |
| 10-23 22:46 | +10 | SOL | DOWN | 0.66 | 0.82 | 1.33 |
| 10-23 22:46 | +5 | SOL | DOWN | 0.66 | 0.73 | 0.40 |
| 10-23 22:46 | +10 stop | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 10-23 22:46 | +20 | XRP | DOWN | 0.66 | 0.92 | 2.39 |
| 10-23 22:46 | +15 | XRP | DOWN | 0.66 | 0.85 | 1.65 |
| 10-23 22:46 | +10 | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 10-23 22:46 | +5 | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 10-23 22:46 | +10 stop | ZEC | DOWN | 0.61 | 0.78 | 1.40 |
| 10-23 22:46 | +20 | ZEC | DOWN | 0.59 | 0.83 | 2.13 |
| 10-23 22:46 | +15 | ZEC | DOWN | 0.59 | 0.78 | 1.60 |
| 10-23 22:46 | +10 | ZEC | DOWN | 0.59 | 0.78 | 1.60 |
| 10-23 22:46 | +5 | ZEC | DOWN | 0.57 | 0.65 | 0.46 |
| 10-23 22:46 | +10 stop | HYPE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-23 22:46 | +20 | HYPE | DOWN | 0.71 | 0.93 | 2.02 |
| 10-23 22:46 | +15 | HYPE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-23 22:46 | +10 | HYPE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-23 22:46 | +5 | HYPE | DOWN | 0.71 | 0.77 | 0.32 |
| 10-23 22:46 | +10 stop | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 10-23 22:46 | +20 | DOGE | DOWN | 0.64 | 0.89 | 2.26 |
| 10-23 22:46 | +15 | DOGE | DOWN | 0.64 | 0.89 | 2.26 |
| 10-23 22:46 | +10 | DOGE | DOWN | 0.64 | 0.75 | 0.79 |
| 10-23 22:46 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
