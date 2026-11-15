# Range-Scalp Bot

*Updated Sun Nov 15 19:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61106 | 53317 | 7789 (114) | 1 | $-16473.11 | -4.3% |
| **+10¢** | 45643 | 36515 | 9128 (153) | 2 | $-15493.51 | -5.4% |
| **+15¢** | 38227 | 28382 | 9845 (191) | 4 | $-14154.07 | -5.9% |
| **+20¢** | 34071 | 23744 | 10327 (243) | 5 | $-12431.82 | -5.8% |
| **+10¢ (15¢ stop)** | 74359 | 74207 | 152 (90) | 1 | $-27347.85 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 19:18 | +5 | XRP | DOWN | 0.70 | open |  |
| 11-15 19:17 | +10 stop | XRP | DOWN | 0.59 | 0.71 | 0.83 |
| 11-15 19:17 | +20 | XRP | DOWN | 0.59 | open |  |
| 11-15 19:17 | +15 | XRP | DOWN | 0.57 | open |  |
| 11-15 19:17 | +10 | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 11-15 19:17 | +5 | XRP | DOWN | 0.58 | 0.65 | 0.36 |
| 11-15 19:17 | +10 stop | ZEC | DOWN | 0.68 | open |  |
| 11-15 19:17 | +20 | ZEC | DOWN | 0.68 | open |  |
| 11-15 19:17 | +15 | ZEC | DOWN | 0.68 | open |  |
| 11-15 19:17 | +10 | ZEC | DOWN | 0.68 | open |  |
| 11-15 19:17 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-15 19:17 | +10 stop | HYPE | DOWN | 0.61 | 0.80 | 1.61 |
| 11-15 19:17 | +20 | HYPE | DOWN | 0.61 | 0.81 | 1.72 |
| 11-15 19:17 | +15 | HYPE | DOWN | 0.61 | 0.80 | 1.61 |
| 11-15 19:17 | +10 | HYPE | DOWN | 0.61 | 0.80 | 1.61 |
| 11-15 19:17 | +5 | HYPE | DOWN | 0.61 | 0.66 | 0.17 |
| 11-15 19:16 | +10 stop | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 11-15 19:16 | +20 | ETH | DOWN | 0.63 | open |  |
| 11-15 19:16 | +15 | SOL | DOWN | 0.66 | 0.83 | 1.44 |
| 11-15 19:16 | +10 | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 11-15 19:16 | +15 | ETH | DOWN | 0.71 | open |  |
| 11-15 19:16 | +10 | ETH | DOWN | 0.70 | open |  |
| 11-15 19:16 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 11-15 19:16 | +10 stop | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 11-15 19:16 | +20 | SOL | DOWN | 0.71 | open |  |
| 11-15 19:16 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
| 11-15 19:16 | +10 stop | DOGE | DOWN | 0.68 | 0.80 | 0.92 |
| 11-15 19:16 | +20 | DOGE | DOWN | 0.67 | open |  |
| 11-15 19:16 | +15 | DOGE | DOWN | 0.67 | open |  |
| 11-15 19:16 | +10 | DOGE | DOWN | 0.67 | 0.80 | 1.02 |
| 11-15 19:16 | +5 | DOGE | DOWN | 0.67 | 0.75 | 0.50 |
| 11-15 19:16 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 11-15 19:16 | +20 | NEAR | DOWN | 0.61 | 0.81 | 1.72 |
| 11-15 19:16 | +15 | NEAR | DOWN | 0.61 | 0.79 | 1.51 |
| 11-15 19:16 | +10 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 11-15 19:16 | +5 | NEAR | DOWN | 0.62 | 0.71 | 0.58 |
| 11-15 19:05 | +10 stop | BTC | UP | 0.66 | 0.85 | 1.65 |
| 11-15 19:05 | +5 | BTC | UP | 0.65 | 0.85 | 1.75 |
| 11-15 19:04 | +10 stop | BTC | DOWN | 0.63 | 0.25 | -4.11 |
| 11-15 19:04 | +10 stop | HYPE | UP | 0.57 | 0.71 | 1.11 |
