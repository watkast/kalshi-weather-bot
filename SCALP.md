# Range-Scalp Bot

*Updated Fri Nov 27 04:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73318 | 63980 | 9338 (165) | 6 | $-19579.32 | -4.2% |
| **+10¢** | 54649 | 43747 | 10902 (210) | 6 | $-18198.84 | -5.3% |
| **+15¢** | 45764 | 34020 | 11744 (268) | 6 | $-16311.76 | -5.7% |
| **+20¢** | 40731 | 28364 | 12367 (334) | 6 | $-14713.41 | -5.8% |
| **+10¢ (15¢ stop)** | 89321 | 89109 | 212 (129) | 5 | $-33024.16 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 04:50 | +10 stop | NEAR | DOWN | 0.60 | open |  |
| 11-27 04:50 | +5 | BNB | DOWN | 0.59 | open |  |
| 11-27 04:50 | +5 | NEAR | DOWN | 0.59 | open |  |
| 11-27 04:50 | +5 | BTC | DOWN | 0.60 | open |  |
| 11-27 04:50 | +5 | HYPE | DOWN | 0.71 | open |  |
| 11-27 04:50 | +10 stop | DOGE | DOWN | 0.63 | open |  |
| 11-27 04:50 | +20 | DOGE | DOWN | 0.63 | open |  |
| 11-27 04:50 | +15 | DOGE | DOWN | 0.63 | open |  |
| 11-27 04:50 | +10 | DOGE | DOWN | 0.63 | open |  |
| 11-27 04:50 | +5 | DOGE | DOWN | 0.63 | open |  |
| 11-27 04:49 | +10 stop | HYPE | DOWN | 0.63 | open |  |
| 11-27 04:49 | +10 | HYPE | DOWN | 0.63 | open |  |
| 11-27 04:49 | +5 | HYPE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-27 04:48 | +10 stop | NEAR | UP | 0.58 | 0.42 | -1.96 |
| 11-27 04:48 | +20 | NEAR | UP | 0.58 | open |  |
| 11-27 04:48 | +15 | NEAR | UP | 0.58 | open |  |
| 11-27 04:48 | +10 | NEAR | UP | 0.58 | open |  |
| 11-27 04:48 | +5 | NEAR | UP | 0.58 | 0.63 | 0.15 |
| 11-27 04:48 | +5 | BNB | DOWN | 0.53 | 0.58 | 0.14 |
| 11-27 04:47 | +5 | ETH | DOWN | 0.67 | 0.74 | 0.39 |
| 11-27 04:47 | +5 | SOL | DOWN | 0.59 | 0.66 | 0.37 |
| 11-27 04:47 | +5 | BTC | DOWN | 0.54 | 0.61 | 0.35 |
| 11-27 04:47 | +10 stop | ZEC | DOWN | 0.57 | 0.68 | 0.76 |
| 11-27 04:47 | +20 | ZEC | DOWN | 0.57 | 0.78 | 1.79 |
| 11-27 04:47 | +15 | ZEC | DOWN | 0.57 | 0.78 | 1.79 |
| 11-27 04:47 | +10 | ZEC | DOWN | 0.57 | 0.68 | 0.76 |
| 11-27 04:47 | +5 | ZEC | DOWN | 0.57 | 0.68 | 0.76 |
| 11-27 04:47 | +10 stop | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 11-27 04:47 | +20 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
| 11-27 04:47 | +15 | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 11-27 04:47 | +10 | ETH | DOWN | 0.60 | 0.71 | 0.78 |
| 11-27 04:47 | +5 | ETH | DOWN | 0.60 | 0.66 | 0.27 |
| 11-27 04:47 | +10 stop | SOL | DOWN | 0.52 | 0.66 | 1.06 |
| 11-27 04:47 | +20 | SOL | DOWN | 0.52 | 0.72 | 1.67 |
| 11-27 04:47 | +15 | SOL | DOWN | 0.52 | 0.72 | 1.67 |
| 11-27 04:47 | +10 | SOL | DOWN | 0.52 | 0.66 | 1.06 |
| 11-27 04:47 | +5 | SOL | DOWN | 0.52 | 0.58 | 0.24 |
| 11-27 04:47 | +10 stop | BNB | DOWN | 0.54 | open |  |
| 11-27 04:47 | +20 | BNB | DOWN | 0.54 | open |  |
| 11-27 04:47 | +15 | BNB | DOWN | 0.54 | open |  |
