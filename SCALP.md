# Range-Scalp Bot

*Updated Thu Nov 19 19:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65398 | 57103 | 8295 (124) | 8 | $-17396.86 | -4.2% |
| **+10¢** | 48834 | 39125 | 9709 (165) | 6 | $-16218.56 | -5.3% |
| **+15¢** | 40952 | 30479 | 10473 (211) | 6 | $-14587.67 | -5.7% |
| **+20¢** | 36464 | 25460 | 11004 (266) | 6 | $-12906.37 | -5.6% |
| **+10¢ (15¢ stop)** | 79619 | 79455 | 164 (98) | 0 | $-29295.32 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 19:26 | +10 stop | SOL | UP | 0.61 | 0.81 | 1.72 |
| 11-19 19:25 | +10 stop | SOL | DOWN | 0.59 | 0.43 | -1.95 |
| 11-19 19:25 | +20 | SOL | DOWN | 0.59 | open |  |
| 11-19 19:25 | +15 | SOL | DOWN | 0.60 | open |  |
| 11-19 19:25 | +10 | SOL | DOWN | 0.60 | open |  |
| 11-19 19:25 | +5 | SOL | DOWN | 0.59 | open |  |
| 11-19 19:24 | +10 stop | DOGE | DOWN | 0.46 | 0.58 | 0.84 |
| 11-19 19:24 | +10 stop | HYPE | UP | 0.70 | 0.54 | -1.93 |
| 11-19 19:23 | +10 stop | DOGE | UP | 0.71 | 0.42 | -3.23 |
| 11-19 19:23 | +10 stop | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 11-19 19:23 | +20 | NEAR | UP | 0.65 | 0.85 | 1.75 |
| 11-19 19:23 | +15 | NEAR | UP | 0.65 | 0.83 | 1.54 |
| 11-19 19:23 | +10 | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 11-19 19:22 | +15 | ZEC | UP | 0.64 | 0.86 | 1.94 |
| 11-19 19:22 | +10 | ZEC | UP | 0.64 | 0.78 | 1.10 |
| 11-19 19:22 | +10 stop | ZEC | UP | 0.70 | 0.48 | -2.52 |
| 11-19 19:22 | +10 stop | SOL | DOWN | 0.61 | 0.73 | 0.89 |
| 11-19 19:22 | +20 | SOL | DOWN | 0.62 | 0.89 | 2.46 |
| 11-19 19:22 | +15 | SOL | DOWN | 0.62 | 0.80 | 1.51 |
| 11-19 19:22 | +10 | SOL | DOWN | 0.62 | 0.73 | 0.79 |
| 11-19 19:22 | +5 | SOL | DOWN | 0.62 | 0.73 | 0.79 |
| 11-19 19:21 | +10 stop | BNB | UP | 0.62 | 0.73 | 0.79 |
| 11-19 19:21 | +10 stop | NEAR | UP | 0.54 | 0.67 | 0.96 |
| 11-19 19:21 | +10 stop | DOGE | UP | 0.57 | 0.67 | 0.66 |
| 11-19 19:21 | +10 stop | BNB | UP | 0.54 | 0.65 | 0.76 |
| 11-19 19:21 | +10 stop | ETH | UP | 0.53 | 0.66 | 0.96 |
| 11-19 19:21 | +10 stop | BTC | UP | 0.54 | 0.68 | 1.06 |
| 11-19 19:20 | +10 stop | NEAR | DOWN | 0.69 | 0.44 | -2.83 |
| 11-19 19:20 | +5 | NEAR | DOWN | 0.69 | open |  |
| 11-19 19:20 | +10 stop | ZEC | DOWN | 0.69 | 0.54 | -1.83 |
| 11-19 19:20 | +5 | ZEC | DOWN | 0.69 | open |  |
| 11-19 19:20 | +10 stop | DOGE | DOWN | 0.59 | 0.36 | -2.64 |
| 11-19 19:20 | +15 | DOGE | DOWN | 0.60 | open |  |
| 11-19 19:20 | +10 | DOGE | DOWN | 0.60 | open |  |
| 11-19 19:20 | +5 | DOGE | DOWN | 0.61 | open |  |
| 11-19 19:19 | +10 stop | ETH | DOWN | 0.66 | 0.50 | -1.94 |
| 11-19 19:19 | +10 stop | BTC | DOWN | 0.66 | 0.50 | -1.94 |
| 11-19 19:18 | +10 stop | BNB | DOWN | 0.58 | 0.40 | -2.15 |
| 11-19 19:18 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 11-19 19:18 | +15 | SOL | DOWN | 0.64 | 0.83 | 1.63 |
