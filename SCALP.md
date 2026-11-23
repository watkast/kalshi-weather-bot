# Range-Scalp Bot

*Updated Mon Nov 23 09:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69757 | 60869 | 8888 (146) | 1 | $-18772.59 | -4.3% |
| **+10¢** | 52059 | 41678 | 10381 (189) | 1 | $-17431.80 | -5.3% |
| **+15¢** | 43627 | 32444 | 11183 (244) | 1 | $-15571.84 | -5.7% |
| **+20¢** | 38845 | 27080 | 11765 (309) | 2 | $-13916.93 | -5.7% |
| **+10¢ (15¢ stop)** | 84951 | 84761 | 190 (118) | 0 | $-31200.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 09:37 | +10 stop | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-23 09:35 | +10 stop | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 11-23 09:35 | +15 | SOL | DOWN | 0.70 | 0.87 | 1.47 |
| 11-23 09:35 | +5 | HYPE | UP | 0.56 | open |  |
| 11-23 09:34 | +10 stop | SOL | UP | 0.53 | 0.33 | -2.34 |
| 11-23 09:34 | +10 stop | ETH | DOWN | 0.69 | 0.83 | 1.15 |
| 11-23 09:34 | +15 | ETH | DOWN | 0.69 | 0.85 | 1.36 |
| 11-23 09:34 | +10 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-23 09:34 | +5 | ETH | DOWN | 0.69 | 0.83 | 1.15 |
| 11-23 09:33 | +10 stop | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-23 09:33 | +15 | BTC | DOWN | 0.70 | 0.88 | 1.57 |
| 11-23 09:33 | +10 | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-23 09:33 | +5 | BTC | DOWN | 0.70 | 0.77 | 0.42 |
| 11-23 09:33 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.29 |
| 11-23 09:32 | +5 | XRP | DOWN | 0.59 | 0.66 | 0.37 |
| 11-23 09:32 | +10 stop | SOL | DOWN | 0.65 | 0.48 | -2.04 |
| 11-23 09:32 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-23 09:32 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.19 |
| 11-23 09:32 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-23 09:32 | +20 | ZEC | DOWN | 0.70 | 0.93 | 2.05 |
| 11-23 09:32 | +15 | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 11-23 09:32 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-23 09:32 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-23 09:31 | +10 stop | SOL | UP | 0.43 | 0.55 | 0.84 |
| 11-23 09:31 | +20 | SOL | UP | 0.43 | open |  |
| 11-23 09:31 | +15 | SOL | UP | 0.43 | 0.60 | 1.35 |
| 11-23 09:31 | +10 | SOL | UP | 0.43 | 0.55 | 0.84 |
| 11-23 09:31 | +5 | SOL | UP | 0.43 | 0.55 | 0.84 |
| 11-23 09:31 | +10 stop | HYPE | UP | 0.67 | 0.51 | -1.94 |
| 11-23 09:31 | +20 | HYPE | UP | 0.67 | open |  |
| 11-23 09:31 | +15 | HYPE | UP | 0.67 | open |  |
| 11-23 09:31 | +10 | HYPE | UP | 0.67 | open |  |
| 11-23 09:31 | +5 | HYPE | UP | 0.67 | 0.74 | 0.40 |
| 11-23 09:31 | +10 stop | DOGE | DOWN | 0.67 | 0.83 | 1.34 |
| 11-23 09:31 | +20 | DOGE | DOWN | 0.68 | 0.90 | 2.01 |
| 11-23 09:31 | +15 | DOGE | DOWN | 0.68 | 0.83 | 1.24 |
| 11-23 09:31 | +10 | DOGE | DOWN | 0.67 | 0.83 | 1.34 |
| 11-23 09:31 | +5 | DOGE | DOWN | 0.67 | 0.83 | 1.34 |
| 11-23 09:31 | +10 stop | BTC | DOWN | 0.60 | 0.76 | 1.30 |
| 11-23 09:31 | +20 | BTC | DOWN | 0.60 | 0.83 | 2.03 |
