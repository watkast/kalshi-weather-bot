# Range-Scalp Bot

*Updated Sat Oct 10 12:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10425 | 8990 | 1435 (22) | 0 | $-3540.70 | -5.4% |
| **+10¢** | 7895 | 6223 | 1672 (36) | 0 | $-3368.21 | -6.8% |
| **+15¢** | 6660 | 4888 | 1772 (52) | 0 | $-2842.51 | -6.8% |
| **+20¢** | 5924 | 4078 | 1846 (66) | 0 | $-2406.07 | -6.5% |
| **+10¢ (15¢ stop)** | 12814 | 12776 | 38 (25) | 0 | $-5014.05 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 12:47 | +10 stop | BNB | DOWN | 0.61 | 0.81 | 1.72 |
| 10-10 12:47 | +20 | BNB | DOWN | 0.61 | 0.81 | 1.72 |
| 10-10 12:47 | +15 | BNB | DOWN | 0.61 | 0.81 | 1.72 |
| 10-10 12:47 | +10 | BNB | DOWN | 0.61 | 0.81 | 1.72 |
| 10-10 12:47 | +5 | BNB | DOWN | 0.61 | 0.70 | 0.58 |
| 10-10 12:47 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-10 12:47 | +20 | BTC | DOWN | 0.66 | 0.88 | 1.96 |
| 10-10 12:47 | +15 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-10 12:47 | +10 | BTC | DOWN | 0.66 | 0.79 | 1.02 |
| 10-10 12:47 | +5 | BTC | DOWN | 0.66 | 0.71 | 0.19 |
| 10-10 12:46 | +10 stop | HYPE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-10 12:46 | +20 | HYPE | DOWN | 0.70 | 0.94 | 2.15 |
| 10-10 12:46 | +15 | HYPE | DOWN | 0.70 | 0.85 | 1.26 |
| 10-10 12:46 | +10 | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 10-10 12:46 | +5 | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-10 12:45 | +10 stop | XRP | DOWN | 0.58 | 0.75 | 1.38 |
| 10-10 12:45 | +20 | XRP | DOWN | 0.58 | 0.79 | 1.80 |
| 10-10 12:45 | +15 | XRP | DOWN | 0.58 | 0.75 | 1.38 |
| 10-10 12:45 | +10 | XRP | DOWN | 0.58 | 0.75 | 1.38 |
| 10-10 12:45 | +5 | XRP | DOWN | 0.58 | 0.64 | 0.25 |
| 10-10 12:45 | +10 stop | SOL | DOWN | 0.57 | 0.69 | 0.87 |
| 10-10 12:45 | +20 | SOL | DOWN | 0.57 | 0.78 | 1.79 |
| 10-10 12:45 | +15 | SOL | DOWN | 0.57 | 0.78 | 1.79 |
| 10-10 12:45 | +10 | SOL | DOWN | 0.57 | 0.69 | 0.87 |
| 10-10 12:45 | +5 | SOL | DOWN | 0.57 | 0.69 | 0.87 |
| 10-10 12:45 | +10 stop | DOGE | DOWN | 0.67 | 0.81 | 1.17 |
| 10-10 12:45 | +20 | DOGE | DOWN | 0.67 | 0.87 | 1.77 |
| 10-10 12:45 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-10 12:45 | +10 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-10 12:45 | +5 | DOGE | DOWN | 0.66 | 0.71 | 0.19 |
| 10-10 12:45 | +10 stop | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 10-10 12:45 | +20 | ZEC | DOWN | 0.58 | 0.82 | 2.11 |
| 10-10 12:45 | +15 | ZEC | DOWN | 0.58 | 0.77 | 1.59 |
| 10-10 12:45 | +10 | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 10-10 12:45 | +5 | ZEC | DOWN | 0.59 | 0.65 | 0.27 |
| 10-10 12:45 | +10 stop | ETH | DOWN | 0.57 | 0.71 | 1.07 |
| 10-10 12:45 | +20 | ETH | DOWN | 0.57 | 0.77 | 1.69 |
| 10-10 12:45 | +15 | ETH | DOWN | 0.57 | 0.74 | 1.38 |
| 10-10 12:45 | +10 | ETH | DOWN | 0.57 | 0.71 | 1.07 |
| 10-10 12:45 | +5 | ETH | DOWN | 0.57 | 0.71 | 1.07 |
