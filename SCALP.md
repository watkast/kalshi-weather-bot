# Range-Scalp Bot

*Updated Sat Nov 21 04:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67010 | 58488 | 8522 (128) | 7 | $-17982.80 | -4.3% |
| **+10¢** | 50042 | 40079 | 9963 (170) | 8 | $-16726.01 | -5.3% |
| **+15¢** | 41962 | 31223 | 10739 (217) | 8 | $-15002.62 | -5.7% |
| **+20¢** | 37349 | 26065 | 11284 (274) | 8 | $-13327.11 | -5.7% |
| **+10¢ (15¢ stop)** | 81589 | 81423 | 166 (100) | 1 | $-30031.07 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 04:05 | +10 stop | HYPE | DOWN | 0.60 | open |  |
| 11-21 04:04 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.90 |
| 11-21 04:04 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-21 04:04 | +10 stop | NEAR | DOWN | 0.59 | 0.73 | 1.09 |
| 11-21 04:04 | +10 stop | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 11-21 04:03 | +10 stop | BNB | DOWN | 0.70 | 0.92 | 2.00 |
| 11-21 04:03 | +5 | SOL | DOWN | 0.66 | 0.71 | 0.19 |
| 11-21 04:03 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 11-21 04:03 | +5 | ZEC | DOWN | 0.63 | open |  |
| 11-21 04:02 | +10 stop | ZEC | UP | 0.48 | 0.61 | 0.95 |
| 11-21 04:02 | +20 | ZEC | UP | 0.48 | 0.71 | 1.97 |
| 11-21 04:02 | +15 | ZEC | UP | 0.46 | 0.61 | 1.15 |
| 11-21 04:02 | +10 | ZEC | UP | 0.46 | 0.61 | 1.15 |
| 11-21 04:02 | +5 | ZEC | UP | 0.46 | 0.55 | 0.54 |
| 11-21 04:02 | +5 | HYPE | UP | 0.70 | open |  |
| 11-21 04:02 | +10 stop | SOL | UP | 0.55 | 0.38 | -2.05 |
| 11-21 04:02 | +20 | SOL | UP | 0.55 | open |  |
| 11-21 04:02 | +15 | SOL | UP | 0.56 | open |  |
| 11-21 04:02 | +10 | SOL | UP | 0.56 | open |  |
| 11-21 04:02 | +5 | SOL | UP | 0.56 | 0.62 | 0.25 |
| 11-21 04:01 | +10 stop | NEAR | UP | 0.64 | 0.47 | -2.05 |
| 11-21 04:01 | +20 | NEAR | UP | 0.64 | open |  |
| 11-21 04:01 | +15 | NEAR | UP | 0.64 | open |  |
| 11-21 04:01 | +10 | NEAR | UP | 0.64 | open |  |
| 11-21 04:01 | +5 | NEAR | UP | 0.65 | open |  |
| 11-21 04:01 | +10 stop | DOGE | UP | 0.56 | 0.39 | -2.05 |
| 11-21 04:01 | +20 | DOGE | UP | 0.56 | open |  |
| 11-21 04:01 | +15 | DOGE | UP | 0.55 | open |  |
| 11-21 04:01 | +10 | DOGE | UP | 0.55 | open |  |
| 11-21 04:01 | +5 | DOGE | UP | 0.55 | open |  |
| 11-21 04:01 | +10 stop | XRP | UP | 0.57 | 0.34 | -2.64 |
| 11-21 04:01 | +20 | XRP | UP | 0.57 | open |  |
| 11-21 04:01 | +15 | XRP | UP | 0.57 | open |  |
| 11-21 04:01 | +10 | XRP | UP | 0.57 | open |  |
| 11-21 04:01 | +5 | XRP | UP | 0.57 | open |  |
| 11-21 04:01 | +10 stop | ETH | UP | 0.52 | 0.36 | -1.95 |
| 11-21 04:01 | +20 | ETH | UP | 0.52 | open |  |
| 11-21 04:01 | +15 | ETH | UP | 0.52 | open |  |
| 11-21 04:01 | +10 | ETH | UP | 0.51 | open |  |
| 11-21 04:01 | +5 | ETH | UP | 0.52 | 0.57 | 0.14 |
