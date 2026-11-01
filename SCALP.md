# Range-Scalp Bot

*Updated Sun Nov 01 17:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43731 | 38107 | 5624 (64) | 2 | $-12467.78 | -4.5% |
| **+10¢** | 32625 | 26128 | 6497 (85) | 3 | $-11196.32 | -5.5% |
| **+15¢** | 27306 | 20308 | 6998 (112) | 3 | $-10236.28 | -6.0% |
| **+20¢** | 24249 | 16918 | 7331 (146) | 3 | $-9037.37 | -5.9% |
| **+10¢ (15¢ stop)** | 53335 | 53249 | 86 (51) | 3 | $-20134.40 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 17:31 | +10 stop | ETH | DOWN | 0.48 | open |  |
| 11-01 17:31 | +20 | ETH | DOWN | 0.48 | open |  |
| 11-01 17:31 | +15 | ETH | DOWN | 0.48 | open |  |
| 11-01 17:31 | +10 | ETH | DOWN | 0.48 | open |  |
| 11-01 17:31 | +5 | ETH | DOWN | 0.47 | 0.54 | 0.34 |
| 11-01 17:30 | +10 stop | HYPE | DOWN | 0.53 | open |  |
| 11-01 17:30 | +20 | HYPE | DOWN | 0.53 | open |  |
| 11-01 17:30 | +15 | HYPE | DOWN | 0.53 | open |  |
| 11-01 17:30 | +10 | HYPE | DOWN | 0.53 | open |  |
| 11-01 17:30 | +5 | HYPE | DOWN | 0.53 | open |  |
| 11-01 17:30 | +10 stop | BTC | DOWN | 0.52 | open |  |
| 11-01 17:30 | +20 | BTC | DOWN | 0.52 | open |  |
| 11-01 17:30 | +15 | BTC | DOWN | 0.52 | open |  |
| 11-01 17:30 | +10 | BTC | DOWN | 0.52 | open |  |
| 11-01 17:30 | +5 | BTC | DOWN | 0.52 | open |  |
| 11-01 17:28 | +10 stop | SOL | DOWN | 0.56 | 0.39 | -2.05 |
| 11-01 17:28 | +20 | SOL | DOWN | 0.56 | yes | -5.78 |
| 11-01 17:28 | +15 | SOL | DOWN | 0.56 | yes | -5.78 |
| 11-01 17:28 | +10 | SOL | DOWN | 0.56 | yes | -5.78 |
| 11-01 17:28 | +5 | SOL | DOWN | 0.56 | yes | -5.78 |
| 11-01 17:26 | +10 stop | XRP | DOWN | 0.55 | 0.30 | -2.83 |
| 11-01 17:25 | +10 stop | XRP | DOWN | 0.57 | 0.67 | 0.66 |
| 11-01 17:18 | +10 stop | BNB | DOWN | 0.66 | 0.45 | -2.44 |
| 11-01 17:18 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-01 17:17 | +10 stop | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-01 17:17 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-01 17:17 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 17:17 | +5 | ETH | DOWN | 0.67 | 0.76 | 0.61 |
| 11-01 17:16 | +10 stop | ETH | UP | 0.52 | 0.62 | 0.65 |
| 11-01 17:16 | +20 | ETH | UP | 0.52 | no | -5.38 |
| 11-01 17:16 | +15 | ETH | UP | 0.52 | no | -5.38 |
| 11-01 17:16 | +10 | ETH | UP | 0.53 | no | -5.48 |
| 11-01 17:16 | +5 | ETH | UP | 0.53 | 0.62 | 0.55 |
| 11-01 17:16 | +10 stop | DOGE | UP | 0.58 | 0.32 | -2.91 |
| 11-01 17:16 | +20 | DOGE | UP | 0.57 | no | -5.88 |
| 11-01 17:16 | +15 | DOGE | UP | 0.57 | no | -5.88 |
| 11-01 17:16 | +10 | DOGE | UP | 0.58 | no | -5.95 |
| 11-01 17:16 | +5 | DOGE | UP | 0.58 | no | -5.95 |
| 11-01 17:16 | +10 stop | HYPE | UP | 0.54 | 0.38 | -1.95 |
| 11-01 17:16 | +20 | HYPE | UP | 0.54 | 0.80 | 2.30 |
