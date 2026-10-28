# Range-Scalp Bot

*Updated Wed Oct 28 13:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38186 | 33317 | 4869 (46) | 0 | $-10772.38 | -4.5% |
| **+10¢** | 28487 | 22857 | 5630 (68) | 0 | $-9605.57 | -5.4% |
| **+15¢** | 23834 | 17790 | 6044 (93) | 0 | $-8546.58 | -5.7% |
| **+20¢** | 21142 | 14812 | 6330 (118) | 0 | $-7513.41 | -5.7% |
| **+10¢ (15¢ stop)** | 46742 | 46675 | 67 (35) | 0 | $-17755.42 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 13:46 | +10 stop | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-28 13:46 | +20 | DOGE | DOWN | 0.71 | 0.94 | 2.05 |
| 10-28 13:46 | +15 | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-28 13:46 | +10 | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-28 13:46 | +5 | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-28 13:46 | +15 | BNB | DOWN | 0.69 | 0.87 | 1.53 |
| 10-28 13:46 | +10 | BNB | DOWN | 0.69 | 0.83 | 1.11 |
| 10-28 13:46 | +5 | BNB | DOWN | 0.69 | 0.76 | 0.38 |
| 10-28 13:46 | +10 stop | XRP | DOWN | 0.64 | 0.78 | 1.10 |
| 10-28 13:46 | +20 | XRP | DOWN | 0.64 | 0.84 | 1.73 |
| 10-28 13:46 | +15 | XRP | DOWN | 0.65 | 0.84 | 1.68 |
| 10-28 13:46 | +10 | XRP | DOWN | 0.65 | 0.78 | 1.05 |
| 10-28 13:46 | +5 | XRP | DOWN | 0.65 | 0.73 | 0.54 |
| 10-28 13:46 | +10 stop | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-28 13:46 | +20 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 10-28 13:46 | +15 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 10-28 13:46 | +10 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-28 13:46 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 10-28 13:46 | +10 stop | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 10-28 13:46 | +20 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
| 10-28 13:46 | +15 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 10-28 13:46 | +10 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 10-28 13:46 | +5 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 10-28 13:46 | +10 stop | ZEC | DOWN | 0.69 | 0.83 | 1.15 |
| 10-28 13:46 | +20 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-28 13:46 | +15 | ZEC | DOWN | 0.70 | 0.87 | 1.50 |
| 10-28 13:46 | +10 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-28 13:46 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
| 10-28 13:46 | +10 stop | BTC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-28 13:46 | +20 | BTC | DOWN | 0.65 | 0.87 | 1.96 |
| 10-28 13:46 | +15 | BTC | DOWN | 0.65 | 0.82 | 1.43 |
| 10-28 13:46 | +10 | BTC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-28 13:46 | +5 | BTC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-28 13:42 | +10 stop | HYPE | DOWN | 0.61 | 0.84 | 1.99 |
| 10-28 13:42 | +20 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 10-28 13:42 | +15 | HYPE | DOWN | 0.63 | 0.84 | 1.83 |
| 10-28 13:42 | +10 | HYPE | DOWN | 0.60 | 0.84 | 2.13 |
| 10-28 13:42 | +5 | HYPE | DOWN | 0.60 | 0.84 | 2.09 |
| 10-28 13:39 | +10 stop | BNB | DOWN | 0.57 | 0.70 | 0.94 |
| 10-28 13:38 | +5 | BNB | UP | 0.61 | no | -6.27 |
