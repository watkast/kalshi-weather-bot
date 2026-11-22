# Range-Scalp Bot

*Updated Sun Nov 22 21:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69099 | 60293 | 8806 (145) | 4 | $-18598.10 | -4.3% |
| **+10¢** | 51566 | 41285 | 10281 (188) | 6 | $-17239.06 | -5.3% |
| **+15¢** | 43213 | 32133 | 11080 (240) | 8 | $-15455.26 | -5.7% |
| **+20¢** | 38481 | 26838 | 11643 (299) | 9 | $-13738.68 | -5.7% |
| **+10¢ (15¢ stop)** | 84146 | 83957 | 189 (117) | 3 | $-30977.99 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 21:09 | +10 stop | DOGE | UP | 0.61 | open |  |
| 11-22 21:09 | +10 stop | BTC | UP | 0.62 | open |  |
| 11-22 21:08 | +10 stop | XRP | UP | 0.61 | open |  |
| 11-22 21:02 | +10 stop | HYPE | UP | 0.70 | 0.84 | 1.15 |
| 11-22 21:02 | +10 | HYPE | UP | 0.70 | 0.84 | 1.15 |
| 11-22 21:02 | +5 | HYPE | UP | 0.70 | 0.84 | 1.15 |
| 11-22 21:02 | +10 stop | ETH | DOWN | 0.58 | 0.26 | -3.52 |
| 11-22 21:02 | +20 | ETH | DOWN | 0.58 | open |  |
| 11-22 21:02 | +15 | ETH | DOWN | 0.58 | open |  |
| 11-22 21:02 | +10 | ETH | DOWN | 0.58 | open |  |
| 11-22 21:02 | +5 | ETH | DOWN | 0.58 | 0.65 | 0.36 |
| 11-22 21:02 | +10 stop | SOL | DOWN | 0.46 | 0.62 | 1.25 |
| 11-22 21:02 | +20 | SOL | DOWN | 0.46 | open |  |
| 11-22 21:02 | +15 | SOL | DOWN | 0.46 | 0.62 | 1.25 |
| 11-22 21:02 | +10 | SOL | DOWN | 0.46 | 0.62 | 1.25 |
| 11-22 21:02 | +5 | SOL | DOWN | 0.46 | 0.62 | 1.25 |
| 11-22 21:02 | +10 stop | BNB | DOWN | 0.67 | 0.50 | -2.04 |
| 11-22 21:02 | +20 | BNB | DOWN | 0.66 | open |  |
| 11-22 21:02 | +15 | BNB | DOWN | 0.66 | open |  |
| 11-22 21:02 | +10 | BNB | DOWN | 0.66 | open |  |
| 11-22 21:02 | +5 | BNB | DOWN | 0.66 | open |  |
| 11-22 21:02 | +5 | NEAR | UP | 0.65 | 0.74 | 0.60 |
| 11-22 21:02 | +10 stop | XRP | DOWN | 0.61 | 0.42 | -2.25 |
| 11-22 21:02 | +20 | XRP | DOWN | 0.61 | open |  |
| 11-22 21:02 | +15 | XRP | DOWN | 0.61 | open |  |
| 11-22 21:02 | +10 | XRP | DOWN | 0.61 | open |  |
| 11-22 21:02 | +10 stop | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 11-22 21:02 | +10 | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 11-22 21:02 | +5 | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 11-22 21:02 | +10 stop | DOGE | DOWN | 0.67 | 0.41 | -2.93 |
| 11-22 21:02 | +20 | DOGE | DOWN | 0.67 | open |  |
| 11-22 21:02 | +15 | DOGE | DOWN | 0.67 | open |  |
| 11-22 21:02 | +10 | DOGE | DOWN | 0.67 | open |  |
| 11-22 21:02 | +5 | DOGE | DOWN | 0.67 | open |  |
| 11-22 21:01 | +10 stop | NEAR | DOWN | 0.46 | 0.30 | -1.93 |
| 11-22 21:01 | +20 | NEAR | DOWN | 0.46 | open |  |
| 11-22 21:01 | +15 | NEAR | DOWN | 0.46 | open |  |
| 11-22 21:01 | +10 | NEAR | DOWN | 0.46 | open |  |
| 11-22 21:01 | +5 | NEAR | DOWN | 0.46 | 0.54 | 0.44 |
| 11-22 21:01 | +10 stop | HYPE | DOWN | 0.53 | 0.63 | 0.65 |
