# Range-Scalp Bot

*Updated Tue Nov 24 09:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70797 | 61798 | 8999 (148) | 0 | $-18906.24 | -4.2% |
| **+10¢** | 52812 | 42303 | 10509 (193) | 0 | $-17508.32 | -5.3% |
| **+15¢** | 44242 | 32923 | 11319 (250) | 0 | $-15576.61 | -5.6% |
| **+20¢** | 39394 | 27477 | 11917 (316) | 0 | $-13941.97 | -5.6% |
| **+10¢ (15¢ stop)** | 86188 | 85990 | 198 (118) | 0 | $-31675.90 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 09:52 | +5 | NEAR | DOWN | 0.63 | 0.72 | 0.58 |
| 11-24 09:51 | +10 stop | HYPE | DOWN | 0.71 | 0.85 | 1.16 |
| 11-24 09:51 | +15 | HYPE | DOWN | 0.71 | 0.86 | 1.26 |
| 11-24 09:51 | +10 | HYPE | DOWN | 0.71 | 0.85 | 1.16 |
| 11-24 09:51 | +5 | HYPE | DOWN | 0.71 | 0.78 | 0.42 |
| 11-24 09:49 | +10 stop | NEAR | DOWN | 0.56 | 0.72 | 1.27 |
| 11-24 09:49 | +10 | NEAR | DOWN | 0.56 | 0.72 | 1.27 |
| 11-24 09:49 | +5 | NEAR | DOWN | 0.56 | 0.62 | 0.21 |
| 11-24 09:47 | +5 | XRP | DOWN | 0.64 | 0.71 | 0.38 |
| 11-24 09:47 | +10 stop | HYPE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-24 09:47 | +20 | HYPE | DOWN | 0.61 | 0.85 | 2.14 |
| 11-24 09:47 | +15 | HYPE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-24 09:47 | +10 | HYPE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-24 09:47 | +5 | HYPE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-24 09:47 | +10 | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 11-24 09:47 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-24 09:47 | +15 | DOGE | DOWN | 0.68 | 0.84 | 1.34 |
| 11-24 09:47 | +10 | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-24 09:47 | +5 | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-24 09:47 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 11-24 09:47 | +10 stop | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 11-24 09:47 | +10 | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 11-24 09:47 | +5 | SOL | DOWN | 0.65 | 0.77 | 0.91 |
| 11-24 09:47 | +10 stop | BNB | DOWN | 0.70 | 0.84 | 1.17 |
| 11-24 09:47 | +20 | BNB | DOWN | 0.68 | 0.89 | 1.87 |
| 11-24 09:47 | +15 | BNB | DOWN | 0.68 | 0.84 | 1.34 |
| 11-24 09:47 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-24 09:47 | +5 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-24 09:46 | +5 | NEAR | DOWN | 0.67 | 0.72 | 0.19 |
| 11-24 09:46 | +10 stop | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 11-24 09:46 | +20 | XRP | DOWN | 0.67 | 0.88 | 1.86 |
| 11-24 09:46 | +15 | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 11-24 09:46 | +10 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 11-24 09:46 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
| 11-24 09:46 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-24 09:46 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 11-24 09:46 | +15 | ETH | DOWN | 0.69 | 0.87 | 1.57 |
| 11-24 09:46 | +10 | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 11-24 09:46 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 11-24 09:46 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
