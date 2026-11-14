# Range-Scalp Bot

*Updated Sat Nov 14 21:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59860 | 52224 | 7636 (107) | 7 | $-16220.65 | -4.3% |
| **+10¢** | 44722 | 35781 | 8941 (143) | 8 | $-15256.09 | -5.4% |
| **+15¢** | 37467 | 27826 | 9641 (180) | 9 | $-13893.21 | -5.9% |
| **+20¢** | 33377 | 23261 | 10116 (232) | 9 | $-12242.32 | -5.8% |
| **+10¢ (15¢ stop)** | 72869 | 72726 | 143 (82) | 2 | $-26787.03 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 21:08 | +10 stop | BNB | DOWN | 0.63 | open |  |
| 11-14 21:08 | +10 stop | SOL | DOWN | 0.44 | 0.54 | 0.64 |
| 11-14 21:07 | +10 stop | ZEC | DOWN | 0.66 | 0.83 | 1.44 |
| 11-14 21:07 | +10 stop | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-14 21:07 | +10 stop | DOGE | UP | 0.57 | 0.21 | -3.90 |
| 11-14 21:07 | +10 stop | BNB | UP | 0.57 | 0.33 | -2.74 |
| 11-14 21:06 | +10 stop | SOL | UP | 0.64 | 0.44 | -2.32 |
| 11-14 21:06 | +10 stop | NEAR | DOWN | 0.59 | 0.76 | 1.40 |
| 11-14 21:06 | +5 | NEAR | DOWN | 0.59 | 0.66 | 0.37 |
| 11-14 21:06 | +10 stop | XRP | DOWN | 0.65 | open |  |
| 11-14 21:06 | +10 stop | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 11-14 21:06 | +10 stop | ZEC | DOWN | 0.69 | 0.50 | -2.23 |
| 11-14 21:06 | +5 | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-14 21:05 | +10 stop | ZEC | UP | 0.52 | 0.33 | -2.21 |
| 11-14 21:05 | +5 | ZEC | UP | 0.52 | 0.60 | 0.45 |
| 11-14 21:05 | +10 stop | BTC | DOWN | 0.60 | 0.72 | 0.88 |
| 11-14 21:04 | +20 | NEAR | UP | 0.61 | open |  |
| 11-14 21:04 | +15 | NEAR | UP | 0.61 | open |  |
| 11-14 21:04 | +10 stop | BNB | UP | 0.64 | 0.35 | -3.23 |
| 11-14 21:04 | +10 stop | HYPE | UP | 0.54 | 0.34 | -2.34 |
| 11-14 21:04 | +10 stop | DOGE | UP | 0.60 | 0.33 | -3.03 |
| 11-14 21:04 | +10 stop | ETH | UP | 0.54 | 0.34 | -2.33 |
| 11-14 21:04 | +10 stop | ZEC | UP | 0.54 | 0.64 | 0.65 |
| 11-14 21:04 | +5 | ZEC | UP | 0.54 | 0.64 | 0.65 |
| 11-14 21:04 | +10 stop | NEAR | UP | 0.60 | 0.26 | -3.71 |
| 11-14 21:03 | +10 stop | SOL | UP | 0.64 | 0.49 | -1.85 |
| 11-14 21:03 | +10 stop | XRP | UP | 0.58 | 0.32 | -2.94 |
| 11-14 21:03 | +10 stop | ZEC | DOWN | 0.52 | 0.30 | -2.53 |
| 11-14 21:03 | +10 stop | BTC | DOWN | 0.62 | 0.41 | -2.44 |
| 11-14 21:03 | +10 stop | ETH | DOWN | 0.65 | 0.40 | -2.83 |
| 11-14 21:03 | +10 stop | NEAR | DOWN | 0.64 | 0.46 | -2.15 |
| 11-14 21:03 | +10 | NEAR | DOWN | 0.65 | 0.76 | 0.82 |
| 11-14 21:03 | +5 | NEAR | DOWN | 0.64 | 0.71 | 0.38 |
| 11-14 21:02 | +10 stop | HYPE | DOWN | 0.66 | 0.51 | -1.84 |
| 11-14 21:02 | +10 stop | NEAR | UP | 0.46 | 0.57 | 0.74 |
| 11-14 21:02 | +20 | NEAR | UP | 0.46 | 0.66 | 1.66 |
| 11-14 21:02 | +15 | NEAR | UP | 0.44 | 0.66 | 1.86 |
| 11-14 21:02 | +10 | NEAR | UP | 0.44 | 0.57 | 0.94 |
| 11-14 21:02 | +5 | NEAR | UP | 0.43 | 0.57 | 1.04 |
| 11-14 21:01 | +10 stop | BNB | UP | 0.70 | 0.51 | -2.23 |
