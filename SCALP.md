# Range-Scalp Bot

*Updated Sun Nov 08 07:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52116 | 45443 | 6673 (82) | 3 | $-14427.53 | -4.4% |
| **+10¢** | 38901 | 31120 | 7781 (107) | 4 | $-13433.74 | -5.5% |
| **+15¢** | 32579 | 24192 | 8387 (137) | 5 | $-12313.75 | -6.0% |
| **+20¢** | 28981 | 20190 | 8791 (181) | 6 | $-10840.19 | -6.0% |
| **+10¢ (15¢ stop)** | 63431 | 63326 | 105 (62) | 3 | $-23430.27 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 07:03 | +10 stop | HYPE | UP | 0.70 | 0.81 | 0.84 |
| 11-08 07:03 | +10 stop | XRP | DOWN | 0.61 | open |  |
| 11-08 07:03 | +20 | XRP | DOWN | 0.61 | open |  |
| 11-08 07:03 | +15 | XRP | DOWN | 0.61 | open |  |
| 11-08 07:03 | +10 | XRP | DOWN | 0.61 | open |  |
| 11-08 07:03 | +5 | XRP | DOWN | 0.61 | open |  |
| 11-08 07:02 | +10 stop | BTC | UP | 0.71 | open |  |
| 11-08 07:02 | +20 | BTC | UP | 0.71 | open |  |
| 11-08 07:02 | +15 | BTC | UP | 0.71 | open |  |
| 11-08 07:02 | +10 | BTC | UP | 0.71 | open |  |
| 11-08 07:02 | +5 | BTC | UP | 0.71 | open |  |
| 11-08 07:02 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.69 |
| 11-08 07:02 | +20 | SOL | UP | 0.64 | open |  |
| 11-08 07:02 | +15 | SOL | UP | 0.64 | open |  |
| 11-08 07:02 | +10 | SOL | UP | 0.63 | 0.74 | 0.79 |
| 11-08 07:02 | +5 | SOL | UP | 0.63 | 0.72 | 0.58 |
| 11-08 07:01 | +10 stop | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 11-08 07:01 | +20 | DOGE | UP | 0.71 | open |  |
| 11-08 07:01 | +15 | DOGE | UP | 0.71 | 0.86 | 1.26 |
| 11-08 07:01 | +10 | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 11-08 07:01 | +5 | DOGE | UP | 0.71 | 0.78 | 0.42 |
| 11-08 07:01 | +10 stop | HYPE | DOWN | 0.56 | 0.34 | -2.58 |
| 11-08 07:01 | +20 | HYPE | DOWN | 0.56 | open |  |
| 11-08 07:01 | +15 | HYPE | DOWN | 0.56 | open |  |
| 11-08 07:01 | +10 | HYPE | DOWN | 0.56 | open |  |
| 11-08 07:01 | +5 | HYPE | DOWN | 0.56 | open |  |
| 11-08 07:01 | +10 stop | NEAR | UP | 0.69 | open |  |
| 11-08 07:01 | +20 | NEAR | UP | 0.69 | open |  |
| 11-08 07:01 | +15 | NEAR | UP | 0.69 | open |  |
| 11-08 07:01 | +10 | NEAR | UP | 0.69 | open |  |
| 11-08 07:01 | +5 | NEAR | UP | 0.69 | 0.74 | 0.21 |
| 11-08 06:56 | +10 stop | ZEC | UP | 0.54 | 0.22 | -3.48 |
| 11-08 06:56 | +10 | ZEC | UP | 0.54 | no | -5.55 |
| 11-08 06:56 | +5 | ZEC | UP | 0.54 | 0.60 | 0.28 |
| 11-08 06:53 | +10 stop | HYPE | UP | 0.63 | 0.81 | 1.52 |
| 11-08 06:53 | +10 stop | ETH | UP | 0.67 | 0.84 | 1.44 |
| 11-08 06:53 | +20 | ETH | UP | 0.67 | 0.89 | 1.97 |
| 11-08 06:53 | +15 | ETH | UP | 0.67 | 0.84 | 1.44 |
| 11-08 06:53 | +5 | ETH | UP | 0.67 | 0.74 | 0.40 |
| 11-08 06:52 | +10 stop | ZEC | DOWN | 0.61 | 0.40 | -2.44 |
