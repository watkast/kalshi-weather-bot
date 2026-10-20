# Range-Scalp Bot

*Updated Tue Oct 20 19:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26077 | 22714 | 3363 (32) | 0 | $-7588.13 | -4.6% |
| **+10¢** | 19625 | 15739 | 3886 (47) | 0 | $-6697.84 | -5.4% |
| **+15¢** | 16429 | 12248 | 4181 (71) | 0 | $-5967.77 | -5.8% |
| **+20¢** | 14534 | 10152 | 4382 (90) | 3 | $-5350.29 | -5.9% |
| **+10¢ (15¢ stop)** | 31962 | 31909 | 53 (30) | 0 | $-11760.30 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 19:05 | +5 | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-20 19:04 | +10 stop | HYPE | DOWN | 0.62 | 0.75 | 0.99 |
| 10-20 19:04 | +20 | HYPE | DOWN | 0.61 | open |  |
| 10-20 19:04 | +15 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 10-20 19:04 | +10 | HYPE | DOWN | 0.62 | 0.75 | 0.99 |
| 10-20 19:04 | +5 | HYPE | DOWN | 0.62 | 0.69 | 0.38 |
| 10-20 19:03 | +10 stop | BTC | DOWN | 0.55 | 0.73 | 1.48 |
| 10-20 19:03 | +20 | BTC | DOWN | 0.55 | open |  |
| 10-20 19:03 | +15 | BTC | DOWN | 0.55 | 0.73 | 1.48 |
| 10-20 19:03 | +10 | BTC | DOWN | 0.55 | 0.73 | 1.48 |
| 10-20 19:03 | +5 | BTC | DOWN | 0.55 | 0.62 | 0.35 |
| 10-20 19:03 | +10 stop | ETH | DOWN | 0.64 | 0.78 | 1.10 |
| 10-20 19:03 | +20 | ETH | DOWN | 0.64 | open |  |
| 10-20 19:03 | +15 | ETH | DOWN | 0.64 | 0.79 | 1.21 |
| 10-20 19:03 | +10 | ETH | DOWN | 0.64 | 0.78 | 1.10 |
| 10-20 19:03 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.23 |
| 10-20 18:53 | +10 stop | ZEC | UP | 0.67 | 0.90 | 2.07 |
| 10-20 18:53 | +10 stop | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 10-20 18:53 | +20 | HYPE | UP | 0.64 | 0.88 | 2.15 |
| 10-20 18:53 | +15 | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 10-20 18:53 | +10 | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 10-20 18:53 | +5 | HYPE | UP | 0.64 | 0.70 | 0.28 |
| 10-20 18:53 | +10 | SOL | UP | 0.63 | 0.88 | 2.25 |
| 10-20 18:53 | +5 | SOL | UP | 0.63 | 0.71 | 0.48 |
| 10-20 18:53 | +5 | BTC | UP | 0.70 | 0.77 | 0.42 |
| 10-20 18:52 | +10 stop | DOGE | UP | 0.53 | 0.64 | 0.75 |
| 10-20 18:51 | +5 | SOL | UP | 0.70 | 0.76 | 0.32 |
| 10-20 18:51 | +10 stop | SOL | UP | 0.71 | 0.88 | 1.47 |
| 10-20 18:51 | +10 stop | ZEC | UP | 0.64 | 0.48 | -1.95 |
| 10-20 18:51 | +10 stop | ETH | UP | 0.67 | 0.85 | 1.55 |
| 10-20 18:51 | +10 stop | BTC | UP | 0.69 | 0.82 | 1.04 |
| 10-20 18:51 | +20 | BTC | UP | 0.69 | 0.93 | 2.17 |
| 10-20 18:51 | +15 | BTC | UP | 0.69 | 0.88 | 1.67 |
| 10-20 18:51 | +10 | BTC | UP | 0.69 | 0.82 | 1.04 |
| 10-20 18:51 | +5 | BTC | UP | 0.69 | 0.74 | 0.21 |
| 10-20 18:49 | +10 stop | ZEC | UP | 0.71 | 0.55 | -1.93 |
| 10-20 18:49 | +10 | ZEC | UP | 0.71 | 0.90 | 1.68 |
| 10-20 18:49 | +5 | ZEC | UP | 0.71 | 0.76 | 0.22 |
| 10-20 18:49 | +10 stop | ETH | UP | 0.69 | 0.52 | -2.03 |
| 10-20 18:49 | +20 | ETH | UP | 0.69 | 0.90 | 1.91 |
