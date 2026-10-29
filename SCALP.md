# Range-Scalp Bot

*Updated Thu Oct 29 17:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39479 | 34467 | 5012 (50) | 3 | $-10957.21 | -4.4% |
| **+10¢** | 29427 | 23636 | 5791 (73) | 5 | $-9694.16 | -5.2% |
| **+15¢** | 24608 | 18385 | 6223 (100) | 6 | $-8649.15 | -5.6% |
| **+20¢** | 21835 | 15316 | 6519 (129) | 7 | $-7524.33 | -5.5% |
| **+10¢ (15¢ stop)** | 48221 | 48151 | 70 (37) | 2 | $-18288.08 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 17:08 | +10 stop | ETH | DOWN | 0.56 | 0.67 | 0.76 |
| 10-29 17:07 | +20 | HYPE | DOWN | 0.64 | open |  |
| 10-29 17:07 | +15 | HYPE | DOWN | 0.64 | open |  |
| 10-29 17:07 | +5 | HYPE | DOWN | 0.64 | open |  |
| 10-29 17:06 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 10-29 17:06 | +10 stop | ETH | DOWN | 0.59 | 0.44 | -1.85 |
| 10-29 17:05 | +10 stop | HYPE | DOWN | 0.68 | 0.51 | -2.04 |
| 10-29 17:05 | +10 | HYPE | DOWN | 0.68 | open |  |
| 10-29 17:05 | +5 | HYPE | DOWN | 0.70 | 0.76 | 0.32 |
| 10-29 17:05 | +10 stop | BTC | DOWN | 0.55 | 0.69 | 1.07 |
| 10-29 17:04 | +5 | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-29 17:04 | +10 stop | DOGE | DOWN | 0.68 | 0.49 | -2.24 |
| 10-29 17:04 | +10 stop | XRP | DOWN | 0.64 | 0.46 | -2.15 |
| 10-29 17:04 | +10 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-29 17:04 | +5 | XRP | DOWN | 0.64 | 0.72 | 0.48 |
| 10-29 17:04 | +10 stop | SOL | DOWN | 0.60 | 0.74 | 1.09 |
| 10-29 17:04 | +10 stop | ZEC | DOWN | 0.54 | open |  |
| 10-29 17:04 | +5 | SOL | DOWN | 0.61 | 0.68 | 0.37 |
| 10-29 17:03 | +10 stop | XRP | UP | 0.48 | 0.58 | 0.64 |
| 10-29 17:03 | +15 | XRP | UP | 0.47 | open |  |
| 10-29 17:03 | +10 | XRP | UP | 0.47 | 0.58 | 0.74 |
| 10-29 17:03 | +5 | XRP | UP | 0.47 | 0.58 | 0.74 |
| 10-29 17:03 | +5 | SOL | UP | 0.45 | 0.57 | 0.84 |
| 10-29 17:03 | +10 stop | DOGE | UP | 0.57 | 0.38 | -2.25 |
| 10-29 17:03 | +10 stop | BTC | UP | 0.58 | 0.40 | -2.15 |
| 10-29 17:03 | +20 | BTC | UP | 0.58 | open |  |
| 10-29 17:03 | +15 | BTC | UP | 0.58 | open |  |
| 10-29 17:03 | +10 | BTC | UP | 0.58 | open |  |
| 10-29 17:03 | +5 | BTC | UP | 0.58 | 0.63 | 0.15 |
| 10-29 17:03 | +10 stop | ETH | UP | 0.63 | 0.36 | -3.04 |
| 10-29 17:03 | +20 | ETH | UP | 0.63 | open |  |
| 10-29 17:03 | +15 | ETH | UP | 0.63 | open |  |
| 10-29 17:03 | +10 | ETH | UP | 0.63 | open |  |
| 10-29 17:03 | +5 | ETH | UP | 0.63 | open |  |
| 10-29 17:03 | +10 stop | ZEC | UP | 0.60 | 0.39 | -2.44 |
| 10-29 17:03 | +20 | ZEC | UP | 0.60 | open |  |
| 10-29 17:03 | +15 | ZEC | UP | 0.59 | open |  |
| 10-29 17:03 | +10 | ZEC | UP | 0.59 | open |  |
| 10-29 17:03 | +5 | ZEC | UP | 0.59 | open |  |
| 10-29 17:02 | +10 stop | SOL | UP | 0.62 | 0.44 | -2.15 |
