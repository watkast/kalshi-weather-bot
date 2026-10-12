# Range-Scalp Bot

*Updated Mon Oct 12 06:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13167 | 11376 | 1791 (25) | 0 | $-4302.35 | -5.2% |
| **+10¢** | 9983 | 7911 | 2072 (37) | 0 | $-4003.64 | -6.4% |
| **+15¢** | 8396 | 6181 | 2215 (55) | 0 | $-3531.61 | -6.7% |
| **+20¢** | 7474 | 5164 | 2310 (70) | 3 | $-3016.71 | -6.4% |
| **+10¢ (15¢ stop)** | 16218 | 16177 | 41 (25) | 0 | $-6363.80 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 06:16 | +10 stop | ZEC | DOWN | 0.58 | 0.76 | 1.49 |
| 10-12 06:16 | +20 | ZEC | DOWN | 0.58 | 0.78 | 1.70 |
| 10-12 06:16 | +15 | ZEC | DOWN | 0.58 | 0.76 | 1.49 |
| 10-12 06:16 | +10 | ZEC | DOWN | 0.58 | 0.76 | 1.50 |
| 10-12 06:16 | +5 | ZEC | DOWN | 0.58 | 0.65 | 0.36 |
| 10-12 06:16 | +10 stop | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-12 06:16 | +20 | ETH | DOWN | 0.66 | open |  |
| 10-12 06:16 | +15 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 10-12 06:16 | +10 | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-12 06:16 | +5 | ETH | DOWN | 0.66 | 0.75 | 0.60 |
| 10-12 06:16 | +10 stop | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 10-12 06:16 | +20 | XRP | DOWN | 0.64 | 0.84 | 1.73 |
| 10-12 06:16 | +15 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-12 06:16 | +10 | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 10-12 06:16 | +5 | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 10-12 06:16 | +10 stop | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-12 06:16 | +20 | DOGE | DOWN | 0.58 | 0.78 | 1.69 |
| 10-12 06:16 | +15 | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-12 06:16 | +10 | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-12 06:16 | +5 | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-12 06:16 | +10 stop | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-12 06:16 | +20 | BTC | DOWN | 0.69 | open |  |
| 10-12 06:16 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-12 06:16 | +10 | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-12 06:16 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
| 10-12 06:16 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-12 06:16 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-12 06:16 | +15 | HYPE | DOWN | 0.69 | 0.85 | 1.36 |
| 10-12 06:16 | +10 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-12 06:16 | +5 | HYPE | DOWN | 0.69 | 0.77 | 0.52 |
| 10-12 06:16 | +10 stop | SOL | DOWN | 0.58 | 0.72 | 1.07 |
| 10-12 06:16 | +20 | SOL | DOWN | 0.58 | 0.78 | 1.69 |
| 10-12 06:16 | +15 | SOL | DOWN | 0.58 | 0.75 | 1.38 |
| 10-12 06:16 | +10 | SOL | DOWN | 0.58 | 0.72 | 1.07 |
| 10-12 06:16 | +5 | SOL | DOWN | 0.58 | 0.72 | 1.07 |
| 10-12 06:16 | +10 stop | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-12 06:16 | +20 | BNB | DOWN | 0.60 | 0.80 | 1.71 |
| 10-12 06:16 | +15 | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-12 06:16 | +10 | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-12 06:16 | +5 | BNB | DOWN | 0.60 | 0.67 | 0.37 |
