# Range-Scalp Bot

*Updated Sat Nov 21 13:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67372 | 58800 | 8572 (134) | 5 | $-18049.57 | -4.3% |
| **+10¢** | 50317 | 40304 | 10013 (175) | 6 | $-16738.55 | -5.3% |
| **+15¢** | 42205 | 31408 | 10797 (225) | 6 | $-14996.12 | -5.7% |
| **+20¢** | 37567 | 26221 | 11346 (283) | 6 | $-13308.46 | -5.6% |
| **+10¢ (15¢ stop)** | 82031 | 81860 | 171 (105) | 0 | $-30112.37 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 13:36 | +10 stop | SOL | DOWN | 0.59 | 0.18 | -4.38 |
| 11-21 13:34 | +10 stop | ZEC | UP | 0.61 | 0.88 | 2.45 |
| 11-21 13:32 | +10 stop | SOL | UP | 0.68 | 0.47 | -2.44 |
| 11-21 13:32 | +10 stop | DOGE | UP | 0.69 | 0.94 | 2.34 |
| 11-21 13:32 | +10 stop | ETH | UP | 0.68 | 0.78 | 0.71 |
| 11-21 13:32 | +10 stop | XRP | UP | 0.63 | 0.76 | 1.00 |
| 11-21 13:31 | +10 stop | XRP | DOWN | 0.61 | 0.33 | -3.13 |
| 11-21 13:31 | +20 | XRP | DOWN | 0.61 | open |  |
| 11-21 13:31 | +15 | XRP | DOWN | 0.61 | open |  |
| 11-21 13:31 | +10 | XRP | DOWN | 0.61 | open |  |
| 11-21 13:31 | +5 | XRP | DOWN | 0.61 | open |  |
| 11-21 13:31 | +10 stop | ZEC | DOWN | 0.63 | 0.47 | -1.95 |
| 11-21 13:31 | +20 | ZEC | DOWN | 0.63 | open |  |
| 11-21 13:31 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-21 13:31 | +10 | ZEC | DOWN | 0.63 | open |  |
| 11-21 13:31 | +5 | ZEC | DOWN | 0.63 | open |  |
| 11-21 13:31 | +10 stop | NEAR | DOWN | 0.58 | 0.35 | -2.60 |
| 11-21 13:31 | +20 | NEAR | DOWN | 0.58 | open |  |
| 11-21 13:31 | +15 | NEAR | DOWN | 0.58 | open |  |
| 11-21 13:31 | +10 | NEAR | DOWN | 0.56 | open |  |
| 11-21 13:31 | +5 | NEAR | DOWN | 0.56 | 0.62 | 0.25 |
| 11-21 13:31 | +10 stop | SOL | DOWN | 0.61 | 0.41 | -2.34 |
| 11-21 13:31 | +20 | SOL | DOWN | 0.61 | open |  |
| 11-21 13:31 | +15 | SOL | DOWN | 0.61 | open |  |
| 11-21 13:31 | +10 | SOL | DOWN | 0.61 | open |  |
| 11-21 13:31 | +5 | SOL | DOWN | 0.61 | open |  |
| 11-21 13:31 | +10 stop | DOGE | DOWN | 0.59 | 0.44 | -1.85 |
| 11-21 13:31 | +20 | DOGE | DOWN | 0.59 | open |  |
| 11-21 13:31 | +15 | DOGE | DOWN | 0.58 | open |  |
| 11-21 13:31 | +10 | DOGE | DOWN | 0.58 | open |  |
| 11-21 13:31 | +5 | DOGE | DOWN | 0.56 | open |  |
| 11-21 13:31 | +10 stop | ETH | DOWN | 0.57 | 0.34 | -2.62 |
| 11-21 13:31 | +20 | ETH | DOWN | 0.56 | open |  |
| 11-21 13:31 | +15 | ETH | DOWN | 0.56 | open |  |
| 11-21 13:31 | +10 | ETH | DOWN | 0.56 | open |  |
| 11-21 13:31 | +5 | ETH | DOWN | 0.56 | open |  |
| 11-21 13:25 | +10 stop | ZEC | UP | 0.67 | 0.86 | 1.65 |
| 11-21 13:25 | +10 stop | NEAR | UP | 0.61 | 0.82 | 1.82 |
| 11-21 13:24 | +10 stop | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 11-21 13:23 | +10 stop | NEAR | DOWN | 0.46 | 0.58 | 0.84 |
