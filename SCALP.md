# Range-Scalp Bot

*Updated Thu Nov 26 01:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72097 | 62936 | 9161 (158) | 4 | $-19135.84 | -4.2% |
| **+10¢** | 53787 | 43086 | 10701 (203) | 5 | $-17743.37 | -5.2% |
| **+15¢** | 45034 | 33508 | 11526 (260) | 6 | $-15832.44 | -5.6% |
| **+20¢** | 40094 | 27955 | 12139 (326) | 6 | $-14222.28 | -5.7% |
| **+10¢ (15¢ stop)** | 87759 | 87550 | 209 (128) | 1 | $-32150.02 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 01:04 | +10 stop | NEAR | UP | 0.51 | open |  |
| 11-26 01:04 | +5 | NEAR | UP | 0.51 | 0.57 | 0.22 |
| 11-26 01:03 | +10 stop | ZEC | UP | 0.67 | 0.47 | -2.34 |
| 11-26 01:02 | +10 stop | HYPE | UP | 0.66 | 0.47 | -2.24 |
| 11-26 01:02 | +10 stop | ETH | UP | 0.70 | 0.81 | 0.84 |
| 11-26 01:02 | +20 | ETH | UP | 0.70 | open |  |
| 11-26 01:02 | +15 | ETH | UP | 0.70 | open |  |
| 11-26 01:02 | +10 | ETH | UP | 0.71 | 0.81 | 0.74 |
| 11-26 01:01 | +5 | NEAR | UP | 0.64 | 0.69 | 0.18 |
| 11-26 01:01 | +10 stop | XRP | UP | 0.61 | 0.81 | 1.72 |
| 11-26 01:01 | +20 | XRP | UP | 0.61 | 0.81 | 1.72 |
| 11-26 01:01 | +15 | XRP | UP | 0.61 | 0.81 | 1.72 |
| 11-26 01:01 | +10 | XRP | UP | 0.61 | 0.81 | 1.72 |
| 11-26 01:01 | +5 | XRP | UP | 0.61 | 0.67 | 0.27 |
| 11-26 01:01 | +10 stop | DOGE | DOWN | 0.53 | 0.25 | -3.12 |
| 11-26 01:01 | +20 | DOGE | DOWN | 0.53 | open |  |
| 11-26 01:01 | +15 | DOGE | DOWN | 0.54 | open |  |
| 11-26 01:01 | +10 | DOGE | DOWN | 0.55 | open |  |
| 11-26 01:01 | +5 | DOGE | DOWN | 0.55 | open |  |
| 11-26 01:01 | +10 stop | BTC | UP | 0.56 | 0.66 | 0.66 |
| 11-26 01:01 | +20 | BTC | UP | 0.57 | 0.82 | 2.21 |
| 11-26 01:01 | +15 | BTC | UP | 0.58 | 0.82 | 2.11 |
| 11-26 01:01 | +10 | BTC | UP | 0.58 | 0.82 | 2.11 |
| 11-26 01:01 | +5 | BTC | UP | 0.58 | 0.66 | 0.46 |
| 11-26 01:01 | +10 stop | SOL | DOWN | 0.51 | 0.35 | -1.94 |
| 11-26 01:01 | +20 | SOL | DOWN | 0.51 | open |  |
| 11-26 01:01 | +15 | SOL | DOWN | 0.51 | open |  |
| 11-26 01:01 | +10 | SOL | DOWN | 0.52 | open |  |
| 11-26 01:01 | +5 | SOL | DOWN | 0.52 | open |  |
| 11-26 01:01 | +10 stop | HYPE | DOWN | 0.58 | 0.33 | -2.88 |
| 11-26 01:01 | +20 | HYPE | DOWN | 0.59 | open |  |
| 11-26 01:01 | +15 | HYPE | DOWN | 0.59 | open |  |
| 11-26 01:01 | +10 | HYPE | DOWN | 0.59 | open |  |
| 11-26 01:01 | +5 | HYPE | DOWN | 0.59 | open |  |
| 11-26 01:01 | +10 stop | NEAR | DOWN | 0.46 | 0.30 | -1.93 |
| 11-26 01:01 | +20 | NEAR | DOWN | 0.46 | open |  |
| 11-26 01:01 | +15 | NEAR | DOWN | 0.46 | open |  |
| 11-26 01:01 | +10 | NEAR | DOWN | 0.46 | open |  |
| 11-26 01:01 | +5 | NEAR | DOWN | 0.46 | 0.55 | 0.54 |
| 11-26 01:01 | +10 stop | ZEC | DOWN | 0.56 | 0.40 | -1.95 |
