# Range-Scalp Bot

*Updated Tue Nov 24 02:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70440 | 61484 | 8956 (147) | 3 | $-18828.21 | -4.2% |
| **+10¢** | 52553 | 42095 | 10458 (190) | 4 | $-17447.67 | -5.3% |
| **+15¢** | 44024 | 32760 | 11264 (246) | 5 | $-15533.65 | -5.6% |
| **+20¢** | 39201 | 27343 | 11858 (311) | 6 | $-13907.09 | -5.7% |
| **+10¢ (15¢ stop)** | 85774 | 85578 | 196 (118) | 2 | $-31526.75 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 02:08 | +10 | ETH | UP | 0.59 | open |  |
| 11-24 02:08 | +5 | ETH | UP | 0.59 | 0.64 | 0.16 |
| 11-24 02:08 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-24 02:08 | +20 | HYPE | DOWN | 0.60 | open |  |
| 11-24 02:08 | +15 | HYPE | DOWN | 0.59 | open |  |
| 11-24 02:08 | +10 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-24 02:08 | +5 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-24 02:07 | +10 stop | XRP | UP | 0.68 | open |  |
| 11-24 02:07 | +10 stop | BNB | DOWN | 0.49 | 0.63 | 1.07 |
| 11-24 02:07 | +20 | BNB | DOWN | 0.46 | open |  |
| 11-24 02:07 | +15 | BNB | DOWN | 0.46 | 0.63 | 1.35 |
| 11-24 02:07 | +10 | BNB | DOWN | 0.47 | 0.63 | 1.25 |
| 11-24 02:07 | +5 | BNB | DOWN | 0.49 | 0.63 | 1.07 |
| 11-24 02:07 | +10 stop | ETH | DOWN | 0.45 | open |  |
| 11-24 02:07 | +20 | ETH | DOWN | 0.42 | open |  |
| 11-24 02:07 | +15 | ETH | DOWN | 0.41 | open |  |
| 11-24 02:07 | +10 | ETH | DOWN | 0.41 | 0.53 | 0.85 |
| 11-24 02:07 | +5 | ETH | DOWN | 0.41 | 0.53 | 0.85 |
| 11-24 02:06 | +10 stop | DOGE | UP | 0.49 | 0.61 | 0.85 |
| 11-24 02:06 | +10 stop | XRP | UP | 0.39 | 0.52 | 0.95 |
| 11-24 02:05 | +10 stop | SOL | DOWN | 0.65 | 0.41 | -2.73 |
| 11-24 02:05 | +20 | SOL | DOWN | 0.65 | open |  |
| 11-24 02:05 | +15 | SOL | DOWN | 0.65 | open |  |
| 11-24 02:05 | +10 | SOL | DOWN | 0.65 | open |  |
| 11-24 02:05 | +5 | SOL | DOWN | 0.66 | open |  |
| 11-24 02:05 | +10 stop | DOGE | DOWN | 0.53 | 0.31 | -2.53 |
| 11-24 02:05 | +20 | DOGE | DOWN | 0.53 | open |  |
| 11-24 02:05 | +15 | DOGE | DOWN | 0.53 | open |  |
| 11-24 02:05 | +10 | DOGE | DOWN | 0.53 | open |  |
| 11-24 02:05 | +5 | DOGE | DOWN | 0.53 | open |  |
| 11-24 02:05 | +10 stop | NEAR | DOWN | 0.55 | 0.69 | 1.07 |
| 11-24 02:05 | +5 | NEAR | DOWN | 0.55 | 0.69 | 1.07 |
| 11-24 02:05 | +10 stop | XRP | DOWN | 0.62 | 0.43 | -2.25 |
| 11-24 02:05 | +20 | XRP | DOWN | 0.62 | open |  |
| 11-24 02:05 | +15 | XRP | DOWN | 0.62 | open |  |
| 11-24 02:05 | +10 | XRP | DOWN | 0.62 | open |  |
| 11-24 02:05 | +5 | XRP | DOWN | 0.62 | open |  |
| 11-24 02:03 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-24 02:03 | +5 | XRP | DOWN | 0.71 | 0.84 | 1.05 |
| 11-24 02:02 | +10 stop | ZEC | DOWN | 0.66 | 0.78 | 0.91 |
