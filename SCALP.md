# Range-Scalp Bot

*Updated Fri Nov 20 00:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65534 | 57204 | 8330 (124) | 5 | $-17558.27 | -4.3% |
| **+10¢** | 48943 | 39202 | 9741 (165) | 7 | $-16336.09 | -5.3% |
| **+15¢** | 41045 | 30539 | 10506 (211) | 7 | $-14694.96 | -5.7% |
| **+20¢** | 36543 | 25504 | 11039 (266) | 7 | $-13028.20 | -5.7% |
| **+10¢ (15¢ stop)** | 79778 | 79614 | 164 (98) | 7 | $-29355.97 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 00:33 | +10 stop | NEAR | DOWN | 0.49 | open |  |
| 11-20 00:33 | +20 | NEAR | DOWN | 0.50 | open |  |
| 11-20 00:33 | +15 | NEAR | DOWN | 0.49 | open |  |
| 11-20 00:33 | +10 | NEAR | DOWN | 0.49 | open |  |
| 11-20 00:33 | +5 | NEAR | DOWN | 0.49 | 0.54 | 0.14 |
| 11-20 00:33 | +10 stop | ETH | DOWN | 0.51 | open |  |
| 11-20 00:33 | +15 | ETH | DOWN | 0.50 | open |  |
| 11-20 00:33 | +10 | ETH | DOWN | 0.51 | open |  |
| 11-20 00:33 | +5 | ETH | DOWN | 0.51 | 0.58 | 0.34 |
| 11-20 00:33 | +10 stop | ZEC | DOWN | 0.61 | open |  |
| 11-20 00:33 | +20 | ZEC | DOWN | 0.61 | open |  |
| 11-20 00:33 | +15 | ZEC | DOWN | 0.61 | open |  |
| 11-20 00:33 | +10 | ZEC | DOWN | 0.61 | open |  |
| 11-20 00:33 | +5 | ZEC | DOWN | 0.61 | open |  |
| 11-20 00:33 | +10 stop | BNB | UP | 0.62 | open |  |
| 11-20 00:33 | +15 | BNB | UP | 0.62 | open |  |
| 11-20 00:33 | +10 | BNB | UP | 0.60 | open |  |
| 11-20 00:33 | +5 | BNB | UP | 0.60 | open |  |
| 11-20 00:33 | +10 stop | HYPE | DOWN | 0.71 | open |  |
| 11-20 00:33 | +20 | HYPE | DOWN | 0.71 | open |  |
| 11-20 00:33 | +15 | HYPE | DOWN | 0.71 | open |  |
| 11-20 00:33 | +10 | HYPE | DOWN | 0.71 | open |  |
| 11-20 00:33 | +5 | HYPE | DOWN | 0.71 | open |  |
| 11-20 00:33 | +10 stop | SOL | DOWN | 0.51 | open |  |
| 11-20 00:33 | +10 stop | DOGE | DOWN | 0.47 | open |  |
| 11-20 00:33 | +20 | DOGE | DOWN | 0.48 | open |  |
| 11-20 00:33 | +15 | DOGE | DOWN | 0.49 | open |  |
| 11-20 00:33 | +10 | DOGE | DOWN | 0.50 | open |  |
| 11-20 00:33 | +5 | DOGE | DOWN | 0.50 | open |  |
| 11-20 00:33 | +10 stop | BNB | DOWN | 0.43 | 0.61 | 1.45 |
| 11-20 00:33 | +20 | BNB | DOWN | 0.44 | open |  |
| 11-20 00:33 | +15 | BNB | DOWN | 0.44 | 0.61 | 1.35 |
| 11-20 00:33 | +10 | BNB | DOWN | 0.44 | 0.61 | 1.35 |
| 11-20 00:33 | +5 | BNB | DOWN | 0.43 | 0.61 | 1.45 |
| 11-20 00:31 | +10 stop | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 11-20 00:31 | +20 | ETH | DOWN | 0.68 | open |  |
| 11-20 00:31 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 11-20 00:31 | +10 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 11-20 00:31 | +5 | ETH | DOWN | 0.68 | 0.74 | 0.30 |
| 11-20 00:30 | +10 stop | SOL | UP | 0.55 | 0.30 | -2.83 |
