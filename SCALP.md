# Range-Scalp Bot

*Updated Mon Oct 12 11:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13534 | 11713 | 1821 (25) | 0 | $-4285.77 | -5.0% |
| **+10¢** | 10252 | 8142 | 2110 (37) | 0 | $-3974.41 | -6.2% |
| **+15¢** | 8624 | 6369 | 2255 (55) | 1 | $-3483.80 | -6.4% |
| **+20¢** | 7677 | 5323 | 2354 (70) | 2 | $-2967.27 | -6.2% |
| **+10¢ (15¢ stop)** | 16644 | 16603 | 41 (25) | 0 | $-6483.11 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 11:47 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-12 11:47 | +20 | HYPE | DOWN | 0.68 | open |  |
| 10-12 11:47 | +15 | HYPE | DOWN | 0.67 | open |  |
| 10-12 11:47 | +10 | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-12 11:47 | +5 | HYPE | DOWN | 0.67 | 0.73 | 0.30 |
| 10-12 11:46 | +10 stop | DOGE | DOWN | 0.63 | 0.83 | 1.70 |
| 10-12 11:46 | +20 | DOGE | DOWN | 0.63 | 0.84 | 1.80 |
| 10-12 11:46 | +15 | DOGE | DOWN | 0.64 | 0.83 | 1.64 |
| 10-12 11:46 | +10 | DOGE | DOWN | 0.64 | 0.83 | 1.64 |
| 10-12 11:46 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.19 |
| 10-12 11:46 | +10 stop | BNB | DOWN | 0.64 | 0.81 | 1.42 |
| 10-12 11:46 | +20 | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 10-12 11:46 | +15 | BNB | DOWN | 0.64 | 0.81 | 1.42 |
| 10-12 11:46 | +10 | BNB | DOWN | 0.64 | 0.81 | 1.42 |
| 10-12 11:46 | +5 | BNB | DOWN | 0.64 | 0.81 | 1.42 |
| 10-12 11:46 | +10 stop | SOL | DOWN | 0.66 | 0.83 | 1.44 |
| 10-12 11:46 | +20 | SOL | DOWN | 0.66 | 0.86 | 1.75 |
| 10-12 11:46 | +15 | SOL | DOWN | 0.66 | 0.83 | 1.42 |
| 10-12 11:46 | +10 | SOL | DOWN | 0.66 | 0.83 | 1.44 |
| 10-12 11:46 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.29 |
| 10-12 11:46 | +10 stop | BTC | DOWN | 0.57 | 0.69 | 0.87 |
| 10-12 11:46 | +20 | BTC | DOWN | 0.57 | 0.77 | 1.69 |
| 10-12 11:46 | +15 | BTC | DOWN | 0.57 | 0.77 | 1.69 |
| 10-12 11:46 | +10 | BTC | DOWN | 0.57 | 0.69 | 0.87 |
| 10-12 11:46 | +5 | BTC | DOWN | 0.57 | 0.69 | 0.87 |
| 10-12 11:46 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-12 11:46 | +20 | ETH | DOWN | 0.71 | open |  |
| 10-12 11:46 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 10-12 11:46 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-12 11:46 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 10-12 11:46 | +10 stop | XRP | DOWN | 0.66 | 0.85 | 1.65 |
| 10-12 11:46 | +20 | XRP | DOWN | 0.65 | 0.85 | 1.75 |
| 10-12 11:46 | +15 | XRP | DOWN | 0.64 | 0.85 | 1.84 |
| 10-12 11:46 | +10 | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 10-12 11:46 | +5 | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 10-12 11:46 | +10 stop | ZEC | DOWN | 0.64 | 0.80 | 1.31 |
| 10-12 11:46 | +20 | ZEC | DOWN | 0.64 | 0.89 | 2.26 |
| 10-12 11:46 | +15 | ZEC | DOWN | 0.64 | 0.80 | 1.31 |
| 10-12 11:46 | +10 | ZEC | DOWN | 0.64 | 0.80 | 1.31 |
| 10-12 11:46 | +5 | ZEC | DOWN | 0.64 | 0.80 | 1.31 |
