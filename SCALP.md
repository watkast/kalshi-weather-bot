# Range-Scalp Bot

*Updated Mon Nov 23 12:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69958 | 61051 | 8907 (146) | 5 | $-18793.96 | -4.3% |
| **+10¢** | 52196 | 41788 | 10408 (189) | 6 | $-17489.29 | -5.3% |
| **+15¢** | 43743 | 32532 | 11211 (245) | 7 | $-15596.77 | -5.7% |
| **+20¢** | 38951 | 27153 | 11798 (310) | 8 | $-13957.09 | -5.7% |
| **+10¢ (15¢ stop)** | 85205 | 85015 | 190 (118) | 3 | $-31292.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 12:33 | +5 | ETH | DOWN | 0.43 | 0.55 | 0.84 |
| 11-23 12:33 | +10 stop | ZEC | UP | 0.62 | open |  |
| 11-23 12:33 | +5 | HYPE | UP | 0.57 | 0.71 | 1.07 |
| 11-23 12:33 | +10 stop | DOGE | UP | 0.53 | 0.72 | 1.57 |
| 11-23 12:33 | +10 stop | BNB | UP | 0.64 | 0.74 | 0.69 |
| 11-23 12:33 | +20 | BNB | UP | 0.64 | open |  |
| 11-23 12:33 | +15 | BNB | UP | 0.64 | open |  |
| 11-23 12:33 | +10 | BNB | UP | 0.64 | 0.74 | 0.69 |
| 11-23 12:33 | +5 | BNB | UP | 0.64 | 0.74 | 0.69 |
| 11-23 12:32 | +5 | ETH | DOWN | 0.57 | 0.63 | 0.25 |
| 11-23 12:32 | +10 stop | HYPE | DOWN | 0.45 | 0.27 | -2.12 |
| 11-23 12:32 | +10 stop | DOGE | DOWN | 0.63 | 0.48 | -1.85 |
| 11-23 12:32 | +20 | DOGE | DOWN | 0.63 | open |  |
| 11-23 12:32 | +15 | DOGE | DOWN | 0.63 | open |  |
| 11-23 12:32 | +10 | DOGE | DOWN | 0.63 | open |  |
| 11-23 12:32 | +5 | DOGE | DOWN | 0.63 | open |  |
| 11-23 12:32 | +10 stop | NEAR | DOWN | 0.62 | 0.35 | -3.03 |
| 11-23 12:32 | +20 | NEAR | DOWN | 0.62 | open |  |
| 11-23 12:32 | +15 | NEAR | DOWN | 0.62 | open |  |
| 11-23 12:32 | +10 | NEAR | DOWN | 0.62 | open |  |
| 11-23 12:32 | +5 | NEAR | DOWN | 0.62 | open |  |
| 11-23 12:32 | +5 | BTC | DOWN | 0.67 | open |  |
| 11-23 12:31 | +10 stop | XRP | DOWN | 0.57 | open |  |
| 11-23 12:31 | +10 stop | ZEC | DOWN | 0.56 | 0.41 | -1.85 |
| 11-23 12:31 | +20 | ZEC | DOWN | 0.56 | open |  |
| 11-23 12:31 | +15 | ZEC | DOWN | 0.56 | open |  |
| 11-23 12:31 | +10 | ZEC | DOWN | 0.56 | open |  |
| 11-23 12:31 | +5 | ZEC | DOWN | 0.56 | open |  |
| 11-23 12:31 | +10 stop | ETH | DOWN | 0.62 | 0.46 | -1.95 |
| 11-23 12:31 | +20 | ETH | DOWN | 0.62 | open |  |
| 11-23 12:31 | +15 | ETH | DOWN | 0.62 | open |  |
| 11-23 12:31 | +10 | ETH | DOWN | 0.62 | open |  |
| 11-23 12:31 | +5 | ETH | DOWN | 0.62 | 0.68 | 0.27 |
| 11-23 12:31 | +10 stop | BTC | DOWN | 0.59 | open |  |
| 11-23 12:31 | +20 | BTC | DOWN | 0.59 | open |  |
| 11-23 12:31 | +15 | BTC | DOWN | 0.59 | open |  |
| 11-23 12:31 | +10 | BTC | DOWN | 0.59 | open |  |
| 11-23 12:31 | +5 | BTC | DOWN | 0.59 | 0.67 | 0.47 |
| 11-23 12:30 | +10 stop | XRP | UP | 0.63 | 0.42 | -2.45 |
| 11-23 12:30 | +20 | XRP | UP | 0.63 | open |  |
