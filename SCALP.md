# Range-Scalp Bot

*Updated Thu Nov 19 14:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65014 | 56742 | 8272 (124) | 1 | $-17484.21 | -4.3% |
| **+10¢** | 48564 | 38888 | 9676 (165) | 2 | $-16264.79 | -5.3% |
| **+15¢** | 40723 | 30287 | 10436 (210) | 3 | $-14676.30 | -5.7% |
| **+20¢** | 36263 | 25303 | 10960 (265) | 7 | $-12979.77 | -5.7% |
| **+10¢ (15¢ stop)** | 79130 | 78966 | 164 (98) | 2 | $-29076.36 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 14:06 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 11-19 14:06 | +5 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 11-19 14:06 | +10 stop | XRP | DOWN | 0.62 | open |  |
| 11-19 14:06 | +10 stop | SOL | DOWN | 0.59 | open |  |
| 11-19 14:06 | +5 | SOL | DOWN | 0.60 | open |  |
| 11-19 14:05 | +5 | SOL | UP | 0.37 | 0.62 | 2.16 |
| 11-19 14:05 | +10 stop | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 11-19 14:04 | +10 stop | XRP | UP | 0.59 | 0.40 | -2.24 |
| 11-19 14:04 | +5 | ZEC | DOWN | 0.68 | 0.77 | 0.61 |
| 11-19 14:03 | +10 stop | SOL | UP | 0.55 | 0.36 | -2.25 |
| 11-19 14:02 | +10 stop | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-19 14:02 | +20 | DOGE | DOWN | 0.70 | open |  |
| 11-19 14:02 | +15 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 11-19 14:02 | +10 | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-19 14:02 | +5 | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-19 14:02 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 11-19 14:02 | +10 stop | HYPE | DOWN | 0.66 | 0.84 | 1.55 |
| 11-19 14:02 | +15 | HYPE | DOWN | 0.68 | 0.84 | 1.32 |
| 11-19 14:02 | +10 | HYPE | DOWN | 0.66 | 0.84 | 1.55 |
| 11-19 14:02 | +5 | HYPE | DOWN | 0.68 | 0.84 | 1.39 |
| 11-19 14:02 | +5 | BNB | DOWN | 0.67 | 0.80 | 1.02 |
| 11-19 14:02 | +10 stop | ZEC | DOWN | 0.61 | 0.77 | 1.30 |
| 11-19 14:02 | +20 | ZEC | DOWN | 0.61 | open |  |
| 11-19 14:02 | +15 | ZEC | DOWN | 0.61 | 0.77 | 1.30 |
| 11-19 14:02 | +10 | ZEC | DOWN | 0.62 | 0.77 | 1.20 |
| 11-19 14:02 | +5 | ZEC | DOWN | 0.63 | 0.70 | 0.38 |
| 11-19 14:02 | +10 stop | SOL | DOWN | 0.50 | 0.61 | 0.75 |
| 11-19 14:02 | +10 stop | XRP | DOWN | 0.61 | 0.42 | -2.25 |
| 11-19 14:02 | +20 | XRP | DOWN | 0.61 | open |  |
| 11-19 14:02 | +15 | XRP | DOWN | 0.61 | open |  |
| 11-19 14:02 | +10 | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 11-19 14:02 | +5 | XRP | DOWN | 0.60 | 0.69 | 0.58 |
| 11-19 14:01 | +10 stop | SOL | UP | 0.55 | 0.40 | -1.85 |
| 11-19 14:01 | +20 | SOL | UP | 0.55 | open |  |
| 11-19 14:01 | +15 | SOL | UP | 0.55 | open |  |
| 11-19 14:01 | +10 | SOL | UP | 0.55 | open |  |
| 11-19 14:01 | +5 | SOL | UP | 0.55 | 0.61 | 0.25 |
| 11-19 14:00 | +10 stop | ETH | DOWN | 0.69 | 0.53 | -1.93 |
| 11-19 14:00 | +20 | ETH | DOWN | 0.69 | open |  |
| 11-19 14:00 | +15 | ETH | DOWN | 0.69 | open |  |
