# Range-Scalp Bot

*Updated Mon Oct 12 01:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12789 | 11039 | 1750 (25) | 4 | $-4222.91 | -5.2% |
| **+10¢** | 9702 | 7678 | 2024 (37) | 4 | $-3949.77 | -6.5% |
| **+15¢** | 8162 | 6006 | 2156 (55) | 6 | $-3436.34 | -6.7% |
| **+20¢** | 7271 | 5023 | 2248 (69) | 8 | $-2940.70 | -6.4% |
| **+10¢ (15¢ stop)** | 15776 | 15735 | 41 (25) | 4 | $-6184.04 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 01:05 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 10-12 01:05 | +15 | HYPE | DOWN | 0.70 | open |  |
| 10-12 01:05 | +10 | HYPE | DOWN | 0.70 | open |  |
| 10-12 01:04 | +10 stop | ZEC | DOWN | 0.48 | open |  |
| 10-12 01:03 | +10 stop | DOGE | UP | 0.65 | 0.75 | 0.72 |
| 10-12 01:03 | +20 | DOGE | UP | 0.65 | open |  |
| 10-12 01:03 | +15 | DOGE | UP | 0.64 | 0.79 | 1.21 |
| 10-12 01:03 | +10 | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 10-12 01:03 | +5 | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 10-12 01:03 | +10 stop | ZEC | UP | 0.64 | 0.40 | -2.74 |
| 10-12 01:03 | +5 | ZEC | UP | 0.64 | open |  |
| 10-12 01:02 | +5 | ETH | UP | 0.69 | open |  |
| 10-12 01:02 | +10 stop | BTC | UP | 0.67 | open |  |
| 10-12 01:02 | +10 stop | HYPE | UP | 0.66 | 0.48 | -2.14 |
| 10-12 01:02 | +10 stop | NEAR | UP | 0.62 | 0.79 | 1.41 |
| 10-12 01:02 | +20 | NEAR | UP | 0.62 | open |  |
| 10-12 01:02 | +15 | NEAR | UP | 0.62 | 0.79 | 1.41 |
| 10-12 01:02 | +10 | NEAR | UP | 0.61 | 0.79 | 1.51 |
| 10-12 01:02 | +5 | NEAR | UP | 0.61 | 0.79 | 1.51 |
| 10-12 01:01 | +5 | HYPE | UP | 0.65 | open |  |
| 10-12 01:01 | +10 stop | SOL | UP | 0.67 | 0.78 | 0.81 |
| 10-12 01:01 | +20 | SOL | UP | 0.67 | open |  |
| 10-12 01:01 | +15 | SOL | UP | 0.66 | open |  |
| 10-12 01:01 | +10 | SOL | UP | 0.66 | 0.78 | 0.91 |
| 10-12 01:01 | +5 | SOL | UP | 0.66 | 0.78 | 0.91 |
| 10-12 01:01 | +10 stop | HYPE | DOWN | 0.57 | 0.35 | -2.57 |
| 10-12 01:01 | +20 | HYPE | DOWN | 0.57 | open |  |
| 10-12 01:01 | +15 | HYPE | DOWN | 0.57 | 0.73 | 1.25 |
| 10-12 01:01 | +10 | HYPE | DOWN | 0.57 | 0.68 | 0.73 |
| 10-12 01:01 | +5 | HYPE | DOWN | 0.57 | 0.63 | 0.21 |
| 10-12 01:01 | +10 stop | XRP | UP | 0.70 | 0.80 | 0.75 |
| 10-12 01:01 | +20 | XRP | UP | 0.70 | open |  |
| 10-12 01:01 | +15 | XRP | UP | 0.70 | open |  |
| 10-12 01:01 | +10 | XRP | UP | 0.70 | 0.80 | 0.75 |
| 10-12 01:01 | +5 | XRP | UP | 0.70 | 0.80 | 0.75 |
| 10-12 01:01 | +10 stop | ETH | UP | 0.66 | open |  |
| 10-12 01:01 | +20 | ETH | UP | 0.66 | open |  |
| 10-12 01:01 | +15 | ETH | UP | 0.66 | open |  |
| 10-12 01:01 | +10 | ETH | UP | 0.66 | open |  |
| 10-12 01:01 | +5 | ETH | UP | 0.66 | 0.75 | 0.60 |
