# Range-Scalp Bot

*Updated Sun Nov 15 19:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61120 | 53331 | 7789 (114) | 1 | $-16465.19 | -4.3% |
| **+10¢** | 45655 | 36527 | 9128 (153) | 0 | $-15479.68 | -5.4% |
| **+15¢** | 38239 | 28394 | 9845 (191) | 0 | $-14134.78 | -5.9% |
| **+20¢** | 34081 | 23754 | 10327 (243) | 0 | $-12411.97 | -5.8% |
| **+10¢ (15¢ stop)** | 74378 | 74226 | 152 (90) | 0 | $-27347.47 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 19:28 | +10 stop | HYPE | UP | 0.52 | 0.65 | 0.96 |
| 11-15 19:28 | +20 | HYPE | UP | 0.54 | 0.89 | 3.30 |
| 11-15 19:28 | +15 | HYPE | UP | 0.55 | 0.89 | 3.17 |
| 11-15 19:28 | +10 | HYPE | UP | 0.52 | 0.65 | 0.95 |
| 11-15 19:28 | +5 | HYPE | UP | 0.52 | 0.65 | 0.96 |
| 11-15 19:26 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 11-15 19:25 | +10 stop | ETH | DOWN | 0.54 | 0.67 | 0.96 |
| 11-15 19:25 | +10 stop | SOL | DOWN | 0.56 | 0.76 | 1.69 |
| 11-15 19:25 | +15 | SOL | DOWN | 0.56 | 0.76 | 1.69 |
| 11-15 19:25 | +10 | SOL | DOWN | 0.55 | 0.76 | 1.79 |
| 11-15 19:25 | +5 | SOL | DOWN | 0.55 | 0.62 | 0.35 |
| 11-15 19:25 | +10 stop | XRP | DOWN | 0.59 | 0.78 | 1.63 |
| 11-15 19:25 | +15 | XRP | DOWN | 0.58 | 0.78 | 1.67 |
| 11-15 19:25 | +10 | XRP | DOWN | 0.58 | 0.78 | 1.73 |
| 11-15 19:25 | +5 | XRP | DOWN | 0.57 | 0.65 | 0.47 |
| 11-15 19:23 | +10 stop | ETH | UP | 0.48 | 0.28 | -2.33 |
| 11-15 19:22 | +10 stop | ZEC | DOWN | 0.56 | 0.68 | 0.86 |
| 11-15 19:22 | +5 | SOL | DOWN | 0.60 | 0.71 | 0.78 |
| 11-15 19:22 | +5 | HYPE | UP | 0.53 | 0.70 | 1.37 |
| 11-15 19:22 | +5 | DOGE | DOWN | 0.70 | 0.78 | 0.52 |
| 11-15 19:21 | +10 stop | XRP | UP | 0.51 | 0.34 | -2.04 |
| 11-15 19:21 | +10 stop | ZEC | UP | 0.57 | 0.38 | -2.22 |
| 11-15 19:21 | +5 | ZEC | UP | 0.57 | open |  |
| 11-15 19:21 | +10 stop | BNB | DOWN | 0.69 | 0.81 | 0.95 |
| 11-15 19:21 | +20 | BNB | DOWN | 0.69 | 0.89 | 1.79 |
| 11-15 19:21 | +15 | BNB | DOWN | 0.69 | 0.86 | 1.47 |
| 11-15 19:21 | +10 | BNB | DOWN | 0.69 | 0.81 | 0.95 |
| 11-15 19:21 | +5 | BNB | DOWN | 0.69 | 0.77 | 0.53 |
| 11-15 19:21 | +10 stop | HYPE | UP | 0.64 | 0.77 | 0.96 |
| 11-15 19:21 | +20 | HYPE | UP | 0.64 | 0.85 | 1.80 |
| 11-15 19:21 | +15 | HYPE | UP | 0.64 | 0.85 | 1.80 |
| 11-15 19:21 | +10 | HYPE | UP | 0.64 | 0.77 | 0.96 |
| 11-15 19:21 | +5 | HYPE | UP | 0.63 | 0.69 | 0.30 |
| 11-15 19:20 | +10 stop | ETH | UP | 0.65 | 0.49 | -1.94 |
| 11-15 19:20 | +5 | ETH | UP | 0.65 | 0.71 | 0.29 |
| 11-15 19:20 | +10 stop | SOL | DOWN | 0.56 | 0.71 | 1.17 |
| 11-15 19:20 | +15 | SOL | DOWN | 0.56 | 0.71 | 1.17 |
| 11-15 19:20 | +10 | SOL | DOWN | 0.56 | 0.71 | 1.17 |
| 11-15 19:20 | +5 | SOL | DOWN | 0.56 | 0.61 | 0.15 |
| 11-15 19:20 | +10 stop | BTC | DOWN | 0.54 | 0.69 | 1.17 |
